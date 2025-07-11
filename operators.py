# Python operators

# * ~~ Arithmetic Operators ~~

# + -> Addition -> 2+3 -> 5
# - -> Subtraction -> 5-2 -> 3
# * -> Multiplication -> 3*4 -> 12
# / -> Division (float) -> 10/3 -> 3.333
# -> // -> Floor division -> 10 // 3 -> 3 
# % -> Mondulus (remainder) -> 10 % 3 -> 1
# ** -> Exponentiation -> 2**3 -> 8

# * ~~ Assignment Operators ~~

# = -> Assign value
x = 5

# += -> Add and assign
x += 3 # x = x + 3

# -= -> Subtract and assign
x -= 2 # x = x - 2

# *= Multiply and assign
x *= 4 # x = x * 4

# /= -> Divide and assign
x /= 2 # x = x / 2

# -> //= -> Floor divide and assign 
x //= 2 # x = x // 2 

# %= -> Modulo and assign 
x %= 3 # x = x % 3

# **= -> Exponentiate and assign
x **= 2 # x = x ** 2

# * ~~ Comparision Operators ~~

# == -> Equal to
3 == 3 # True

# != -> Not equal to
5 != 3 # True

# > -> Greater than
5 > 2 # True

# < -> Less than
3 < 1 # False

# >= -> Greater than or equal
4 >= 4 # True

# <= -> Less than or equal
2 <= 3 # True

# * ~~ Logical Operators ~~

# and -> True if both
True and False # False

# or -> True if atleast 1
True or False # True

# not -> Inverts the value
not True # False

# * ~~ Bitwise Operators ~~

# & -> Bitwise AND
5 & 3 # 1 -> 101 & 011 = 001

# ` -> ` -> Bitwise OR
# `5

# ^ -> Bitwise XOR (exclusive OR)
5 ^ 3 # 6 -> 101 ^ 011 = 110

# ~ -> Bitwise NOT (Invert)
~5 # -6 -> -101 = -110

# << -> Shift left
2 << 2 # 8 -> 10->1000 (Multiply by 4)

# >> -> Shift right
8 >> 2 # 2 -> 1000->10 (Divide by 4)

# * ~~ Identity Operators ~~

# is -> Same object in memory
# a is b -> True if same object

# is not -> Not same object
# a is not b -> True if different

# * ~~ Membership Operators ~~

# in -> value exists
'a' in 'cat' # True

# not in -> Value dosn't exist
5 not in [1, 2] # True

# * ~~ Ternary Operator ~~

# Shortcut for is-else statement
x = 5
result = "even" if x % 2 == 0 else "odd"

# * ~~ Operator Precedence ~~
#? Some operators take priority (like in math)

# Order (High -> Low):

# () -> Parentheses
# ** -> Exponent
# +, - (Unary)
# *, /, //, % 
# +, -
# Comparison (==, !=, <, > etc)
# not
# and
# or
