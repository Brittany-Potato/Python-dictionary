
# Functions

# * ~~ Information and help ~~

# help() -> Displays help about an object
help(str)

# dir() -> List attributes and methods of an objects
dir(list)

# type() -> Returns the type of an object
type(5) # -> <class 'int'>

# id() -> Returns memory ID of an object
id("hello")

# isinstance() -> Checks object type
isinstance(5, int) # -> True

# callable() -> Checks if an object is callable
callable(print) # -> True

# eval() -> Evaluates a string as Python code #! (risky)

# * ~~ Numeric Functions ~~

# abs() -> Absolute value
abs(-7) # 7

# round() -> Rounds number
round(3.1415, 2) # -> 3.14

# pow() -> Exponentiation (x ** y)
pow(2, 3) # 8

# divmod() -> Returns quotient and remainder
divmod(7, 3) # -> (2, 1)

# sum() -> Sum of iterable
sum([1, 2, 3]) # -> 6

# min() -> Smallest value in iterable
min([1, 3, 2]) # -> 1

# max() -> Largest value in iterable
max([1, 2, 3]) # -> 3

# * ~~ String and Character Functions ~~

# chr() -> Converts int to Unicode character
chr(97) # -> 'a'

# ord() -> Converts character to Unicode int
ord('a') # -> 97

# format() -> Returns formatted string
format(3.14159, ".2f") # -> '3.14'

# * ~~ Iterable and Collection Functions ~~

# len() -> Length of iterable
len("hello") # -> 5

# sorted() -> Returns a new sorted list
sorted([3, 1, 2]) # -> [1, 2, 3]

# reversed() -> Reverses iterable 
list(reversed("abc")) # -> ['c', 'b', 'a']

# enumerate() -> Index + value pairs
list(enumerate(['a', 'b'])) # -> [(0, 'a')]

# zip() -> Combines iterables into tuples
zip([1,2],[3,4]) [(1,3), (2,4)]

# map() -> Applies a function to all items
list(map(str.upper, ['a', 'b'])) # -> ['A', 'B']

# filter() -> Filters iterable by function
list(filter(lambda x: x > 0, [-1, 2])) # -> [2]

# all() -> Checks if all items are True
all([True, True]) # -> True

# any() -> Checks if any item is True
any([False, True]) # -> True

# * ~~ Object and Variable Functions ~~

# vars() -> Returns __dict__ attribute of an object
