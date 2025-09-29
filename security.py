# Overview of essential security practices in Python.

#! Security is a complex field. Always use trusted, well-maintained libraries
#! For critical tasks like cryptography and authetication. Never roll your own.

import os
import time
import bcrypt
import sqlite3
import html
from getpass import getpass

#* ~~ Secure Password Handling ~~

#? Why: Storing passwords in plain text is extremely dangerous. If your database is
#? ever compromised, attackers will have the credentials for every user.
#? Passwords must be "hashed" using a strong, slow algorithim.

# What is Hashing / Salting
# Hashing is a one-way process that turns a password into a fixed-length string of
# characters (the 'hash'). It cannot be reversed.
# A "salt" is a random string added to each password before hashing. This ensures
# that even if two users have the same password, their hashes will be different,
# which protects against 'rainbow table' attacks.

# GOOD: Use a dedicated library like 'bcrypt' or 'passlib'
# To install: pip install bcrypt

def hash_password(plain_text_password):
    # Hashes a password with randomly generated salt
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed_bytes

def check_password(plain_text_password, hashed_password):
    # Checks if a plain text password matches a stored hash
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

# -- Example --
# password = getpass("Enter a new password: ")
# hashed = hash_password(password)
# print(f"Storing this in the database: {hashed}")

# login_attempt = getpass("Enter your password to log in: ")
# if check_password(login_attempt, hashed):
#       print("Login successful")
# else:
#   print("Password incorrect")

#* ~~ Preventing Bruteforce attacks ~~ 

#? Why: A brute-force attack is when an attacker repeatedly tries different
#? passwords to guess the correct one. Without protection, an automated script
#? Can make thousands of attempts per minute.

# This is a simplified, conceptual example. In a real app, you would use
# a database, Redis, or a dedicated middleware library.

login_attempts = {} # Store {ip: [timestamp1, timestamp2, ...]}
MAX_ATTEMPTS = 5
TIMEFRAME = 60 # Seconds

def is_rate_limited(ip_address):
    # Checks if an IP address has made too many requests recently
    current_time = time.time()
    
    # Get recent attempts for this IP
    if ip_address not in login_attempts:
        login_attempts[ip_address] = []
        
    recent_attempts = [t for t in login_attempts[ip_address] if current_time - t < TIMEFRAME]
    login_attempts[ip_address] = recent_attempts
    
    if len(recent_attempts) >= MAX_ATTEMPTS:
        print(f"IP {ip_address} is rate-limited. Try again later.")
        return True
    
    login_attempts[ip_address].append(current_time)
    return False

# Second option - Account lockout 

#? Temporarily locks an account after a certain number of consecutive failed attempts.
#? This is also a conceptual example. You would store the faliure count in your user database.
user_faliure_count = {}

def handle_failed_login(username):
    user_faliure_count[username] = user_faliure_count.get(username, 0) + 1
    if user_faliure_count[username] >= 5:
        print(f"Account for {username} is locked due to too many failed attempts.")
        # In a real app you would set a flag in the database.
        

#* ~~ Preventing SQL injection ~~

#? Why: SQL Injection allows an attacker to interfere with the queries that an
#? application makes to its database. It can be used to read sensitive data,
#? modify data, or even execute administrative commands on the database.

#! BAD: Neever use string formatting (f-string, %, .format()) to build queries!
# An attacker could enter: ' OR 1=1 --
# The final query would become: "SELECT * FROM users WHERE username = '' OR 1=1 --' AND password = '...'"
# This would log them in as the first user without a password.

def insecure_login(username, password):
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    #! HIGHLY VULNERABLE
    
#* GOOD: Use Parameterized Queries (Prepared statements)
# The database driver treats the SQL command and the user data seperately,
# So the user input can never be misinterpreted as part of the command.

def secure_login(username):
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()
    # The '?' is a placeholder. The driver safely inserts the variable
    # For MySQL/PostgreSQL, the placeholder might be '%s'.
    cursor.execute("SELECT * FROM users WHERE username = ?", (username))
    return cursor.fetchone()


#* ~~ Preventing Cross-site scripting (XSS) ~~

#? Why: XSS allows attackers to inject malicious scripts (Usually JavaScript) into
#? web pages viewed by other users. This can be used to steal session cookies,
#? deface websites, or redirect users to malicious sites.

# The solution is to "escape" user-provided data before displaying it in HTML.
# This means converting special HTML characters like '<', '>', '&' into their
# safe equivalents ('&lt;','&gt' ,'&amp')

# Most web frameworks (Django, Flask/Jinja2) do this automatically.
# But if you are ever generating HTML manually, you must do it yourself.

#! BAD: Directly inserting user input into an HTML template.
user_comment = "<script>alert('You have been hacked!');</script>"
# html_output = f"<p>Latest Comment: {user_comment}</p>" #VULNERABLE

#* GOOD: Use a library to escape the HTML
safe_comment = html.escape(user_comment)
html_output = f"<p>Latest comment: {safe_comment}</p>"
# The output will be:
# <p>Latest Comment: &lt;script&gt;alert('You have been hacked!');&lt;/script&gt;</p>
# This will be displayed as text to the user and the script will not run.
# print(html_output)

#* ~~ Securely handling secrets (API keys, passwords etc) ~~

#? Why: Never hardcode secrets directly into your sourcecode. If you commit the 
#? code to a public repository (like GitHub), your secrets will be exposed.

#! BAD: Hardcoding secrects in the code
# api_key = sk_this_is_a_very_secret_key_12345 #! VERY BAD

#* GOOD: Use enviroment variables
# Store secrets in the envrionment where the application runs.
# In development, you can use a '.env' file and a library like 'python-dotenv'.
# To install: pip install python-dotenv

# In your .env file (Which you NEVER commit to version control):
# DATABASE_PASSWORD = "my-secret-database-password"
# API_KEY = "sk_123456789"

# from dotenv import load_dotenv
# load_dotenv() # Loads variables fromt he .env file

db_password = os.getenv("DATABASE_PASSWORD")
api_key = os.getenv("API_KEY")

if not db_password or not api_key:
    print("A required secret is not in the environment!")
else:
    print("Successfully loaded secrets.")