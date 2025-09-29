# Error handling

# * ~~ Try/Except ~~

# try:
    # Code that might raise an error
# except ValueError:
    # Code that runs if the error occurs
    
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
    
# * ~~ Catching Multiple Exceptions ~~

try:
    reult = 10 / int(input("Enter a number: "))
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("You must enter a number")
    
# You can also catch multiple exceptions in one line
# except (ZeroDivisionError, ValueError):

# * ~~ Catching All Exceptions ~~
# ! Use with caution

risky_code = "Stop screaming at me about squiggles"

try:
    # This code will cause a ZeroDevisionError
    result = 10 / 0
except Exception as e:
    # The 'e' variable contains the exception object
    print(f"An error occured: {e}")
    print(f"The type of error was: {type(e).__name__}")
    
# * ~~ else Clause ~~

# Runs only if no exception occurs
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", number)
    
# * ~~ finally Clause

try:
    f = open("data.txt")
    content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("This always runs")
    if 'f' in locals():
        f.close

# * ~~ raise - Manually Triggers Errors ~~

# You can raise exceptions yourself
age = -1
if age < 0:
    raise ValueError("Age can't be negative")

# * ~~ Custom Exceptions ~~

# You can create your own error types by subclassing Exception
class TooSmallError(Exception):
    pass

value = 3
if value < 5:
    raise TooSmallError("Value is too small")
# And catch it
try:
    raise TooSmallError("Oops")
except TooSmallError as e:
    print(e)
    
# * ~~ The 'with' Statement (Context managers) ~~

#? The 'with' statement simplifies resource management (like files) by ensuring
#? that cleanup operations (like f.close()) are always performed,
#? even if an error occurs inside the block. It is the recommended way to handle files.

# This code is cleaner and safer than the try/finally block for files.
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found. The 'with' statement already handled closing.")


    
# * ~~ Common Built-in Exceptions ~~

# ValueError -> Invalid value (e.g., int("abc"))

# TypeError -> Wrong types (e.g., adding string to int)

# ZeroDivisionError -> Division by zero

# IndexError -> List index out of range

# KeyError -> Dictionary key not found

# FileNotFoundError -> File does not exist

# AttributeError -> Object has no such attribute

# ImportError -> Module/Function can't be imported

# NameError -> A variable is not found (e.g. print(my_variable) before it is defined)

# SyntaxError -> The code s not valid python (e.g. missing a colon)

# IndentationError -> Incorrect indentation

# KeyboardInterupt -> The user hits Ctrl + c

#* ~~ Assert - for debugging ~~
# Raises an AeertationError if a condition is not met.
# Can be disabled  in production for performance.

user_role = 'guest'
assert user_role == "admin", "User must be an admin to proceed!"
# This will raise: AssertionError: User must be an admin to proceed!


