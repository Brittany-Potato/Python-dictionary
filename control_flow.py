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
    print("Counting:" count)
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
# if x > 5: pass

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
        
