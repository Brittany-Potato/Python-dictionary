# Control flow in Python

# * ~~ Conditional Statements ~~

# if
age = 20
if age >= 18:
    print("You're an adult")
    
    
# if - else
if age >= 18:
    print("You're an adult")
else:
    print("You're a minor")
    
    
# if - elif - else
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
    

# * ~~ Loops ~~
# Repeat this action

# for loops - iterates over a sentance
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
    
# for with range()
for i in range(3):
    print(i) # 0, 1, 2
    
# while loops - Repeat while a condition is true
count = 0
while count < 3:
    print("Counting:", count)
    count += 1
    # Make sure the condition will eventually become false or you get an infinite loop
    
# * ~~ Loop control Statements ~~


# break -> exit the loop early
# if x == 5: break
for i in range(10):
    if i == 3:
        break
    print(i) # Output: 0 1 2

# continue -> skip the current iteration
# if x % 2 == 0: continue
for i in range(5):
    if i == 2:
        continue
    print(i) # Output: 0 1 3 4

# pass -> Do nothing (placeholder)
# Useful when a statement is syntactically required but you have nothing to write yet.
def my_future_function():
    pass # I'll write the code for this later

class MyEmptyClass:
    pass

#* ~~ Loop with an 'else' Clause ~~
#? The 'else' block runs only if the loop finishes without encountering a 'break'.
# 
# # Example: Search for an item in a list
my_list = [1,2,3,4]
for item in my_list:
    if item == 5:
        print("Found 5!")
        break
else: # This 'else' belongs to the 'for' loop
    print("Did not find 5 in the list") # Output: Did not find 5 in the list 


# * ~~ Nested Control Flow ~~

for i in range(3):
    if i % 2 == 0:
        print(f"{i} if event")
    else:
        print(f"{i} is odd")
        
# * ~~ Match/Case (Python 3.10+)
#? Similiar to switch in other languages. Used for multiple-choice logic

command = "start"

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
        

#* ~~ Comprehensions ~~
#? A concise, Pythonic way to create collections (lists, sets, dicts) from iterables.

# List comprehension
# Creates a new list of squares from 0 to 4
squares = [i**2 for i in range(5)]
# -> [0, 1, 4, 9, 16]

# You can also add a condition
even_squares = [i**2 for i in range(10) if i % 2 == 0]
# -> [0, 4, 16, 36, 64]

# Dictionary Comprehension 
square_dict = {i: i**2 for i in range(5)}
# -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension 
unique_squares = {i**2 for i in [1, 1, 2, 2, 3]}
# -> {1, 4, 9}

#* ~~ Advanced Match/Case (Python 3.10+) ~~

# More advanced example with multiple matches and value capturing
http_status = 404
match http_status:
    case 200 | 201: #Match multiple literal values
        print("Success")
    case 404:
        print("Not found")
    case status_code if status_code >= 500: # Capture value and use a guard
        print(f"Server Error: {status_code}")
    case _: # Wildcard case
        print("Other Error")