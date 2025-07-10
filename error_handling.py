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
    risky_code()
except Exception as e:
    print("An error occurred:", e)
    
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
    
# * ~~ Common Built-in Exceptions ~~

# ValueError -> Invalid value (e.g., int("abc"))

# TypeError -> Wrong types (e.g., adding string to int)

# ZeroDivisionError -> Division by zero

# IndexError -> List index out of range

# KeyError -> Dictionary key not found

# FileNotFoundError -> File does not exist

# AttributeError -> Object has no such attribute

# ImportError -> Module/Function can't be imported

