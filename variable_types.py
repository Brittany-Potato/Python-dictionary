# Variable Types (Data types)

# * ~~ Numeric Types ~~

# int -> Integer (Whole numbers)
x = 5

# float -> Decimial numbers
y = 3.14

# complex -> Complex numbers
z = 2 + 3j

# * ~~ Text Types ~~

# str -> string of text
greeting = "Hello, world!"

# * ~~ Booleans Types ~~

# bool -> True or false values
is_on = True

# * ~~ Sequence Types ~~

# list -> Ordered, changeable, allows dupes
[1,2,3]

# tuple -> Ordered, immutable, allows dupes
(1,2,3)

# range -> Immutable sequence of numbers 
range(5) # -> 0,1,2,3,4

# * ~~ Set Types ~~

# set -> Unique, unordered 
{1,2,3}

# frozenset -> Immutable set
frozenset([1, 2])

# * ~~ Mapping Types ~~

# dict -> Key-value mapping -> {"name": "Brittany", "age": 27}

person = {
    "name": "Britt",
    "age": 27
}

# * ~~ Binary Types ~~

# bytes -> Immutable binary
b"Hello"

# bytearray -> Mutable binary
bytearray([65, 66, 67])

# memoryview -> Memory-efficent 
memoryview(b"abc")

# * ~~ None Type ~~

# NoneType -> No value/Null
value = None

# * ~~ Type Checking ~~

# Use type() function:
print(type("Hello")) # <class 'str'>

# * ~~ Type Conversion Examples ~~

int("42") # -> 42
float("3.14") # -> 3.14
str(123) # -> '123'
list('abc') # -> ['a', 'b', 'c']
dict([("a", 1)]) # -> {'a': 1}