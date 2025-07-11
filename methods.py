# In python "Methods" usually refer to functions that are associated with objects, 
# expecially class instances or built-in types like str, list, dist etc

# Includes Built-in data types, special methods and common objects via OOP

# * ~~ String Methods ~~

#? A 'String Method' in python is a built-in function that operates on a string object. 
#? It lets you perform common tasks on strings like changing case, searching, replacing text, splitting and more.

# upper() 
"hello".upper() # -> "HELLO"

# lower() 
"HELLO".lower() # -> "hello"

# strip() 
" hi".strip() # -> "hi"

# replace()
"dog".replace("d", "l") # -> "log"

# split()
"a,b,c".split(",") # -> ['a', 'b', 'c']

# find()
"hello".find("e") # -> 1

# startswith()
"hello".startswith("he") # -> True

# endswith()
"hello".endswith("lo") # -> True

# * ~~ List Methods ~~

#? 'List Methods' are built- in functions that can be used to 
#? modify, access, or manipulate lists (a mutable, ordered collection of items)

mylist = [1,2,3]

# append()
mylist.append(4) # -> [1,2,3,4] Adds 4 onto the end

# extend()
mylist.extend([5,6]) # -> [1,2,3,4,5,6] extends the list with the numbers specified

# insert()
mylist.insert(1, "hi") # -> [1, "hi",2,3,4,5,6] inserts "hi" into the index of "1"

# pop()
mylist.pop() # -> [1, "hi",2,3,4,5] Removes the last item i.e "6"

# remove()
mylist.remove("hi") # -> [1,2,3,4,5] Removes the item specified

# reverse()
mylist.reverse() # -> [5,4,3,2,1] Reverses the list

# sort()
mylist.sort() # -> [1,2,3,4,5] Sorts the list in ascending order

# * ~~ Dictionary Methods ~~

#? 'Dictionary Methods' are built-in functions that work on dictionaries (dict types) 
#? to help you access, modify, or managing key-value pairs.

mydict = {"a": 1, "b": 2}

# get()
mydict.get("key", "default") # -> "default" - "key" doesnt exist so "default" is returned

# keys()
mydict.keys() # Returns a view of all keys in the dictionary

# values()
mydict.values() # Returns a view of all values in the dictionary

# items()
mydict.items() # Returns key-value pairs

# update()
mydict.update({"a": 1}) # Updateds the value for key "a" to 1 (It was already 1 so there is no change)

# pop()
mydict.pop("a") # -> 1 - Removes the key "a" and returns its value

# clear()
mydict.clear() # Removes all keyvalue pairs from the dictionary mydict = {}

# * ~~ Set Methods ~~

myset = {1, 2, 3, 4} 

# add()
myset.add(4) # -> {1, 2, 3, 4} - Set already had 4 so it has no effect

# update() 
myset.update([5, 6]) # -> {1, 2, 3, 4, 5, 6}

# remove()
myset.remove(4) # -> {1, 2, 3, 5, 6} - Removes 4 from the set

# discard()
myset.discard(5) # -> {1, 2, 3, 6} Removes 5 and does not raise an error if the element is missing

a = {1, 2, 3}
b = {3, 4, 5}

# union()
a.union(b) # -> {1, 2, 3, 4, 5} - Returns a new set with all elements from a and b 

# intersection()
a.intersection(b) # -> {3} - Returns a new set with elements common to both a and b 

# difference()
a.difference(b) # -> {1, 2} - Returns a new set with elements in a but not b

# * ~~ Trupe Methods ~~

t = (1,2, 2, 3)

# count()
t.count(1) # 1 - 1 only appears once

# index()
t.index(2) # 1 - returns the first index where the value 2 appears. In this case it is position 1

# * ~~ File Methods ~~

with open("file.txt", "w") as f:
    f.write("Hello\n")

# read()
f.read() # -> Hello - Reads the entire file contents

# readline()
f.readline() # -> Hello - Reads just the first line

# readlines
f.readlines() # -> ['Hello\n'] - Returns a list of all lines in the file

# write()
f.write("text") # -> Hello text - Appends "text" to the file

# close()
f.close() # -> Not needed/used with using with because it auto closes

# seek()
f.seek(0) # -> Hello text - Moves the cursor back to the beginning of the file, so you can re-read it

# * ~~ Class special Methods (Dunder Methods) ~~

# __init__() -> Object creation 

# __str__() -> str(obj) or print(obj)

#__repr__() -> repr(obj)

#__len__() -> len(obj) 

#__getitem__() -> obj[key] = value

#__iter__() -> looping

# * ~~ Object-Oriented Methods (Instance Methods) ~~

class Dog:
    def __init__(self, name):
        self.name = name
        
    def back(self):
        print(f"{self.name} says woof!")
        
fido = Dog("Fido")
fido.bark() # Fido says woof

# * ~~ Statis and Class Mathods ~~

# Static method -> @staticmethods

# Class method -> @classmethod

class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def identity(cls):
        return cls
print(Math.add(2, 3)) # 5
print(Math.identity()) # <class '__main__.Math'>

# * ~~ Other Nobel Built-in Object Methods ~~

# __call__() -> Makes object callable

# __enter__() & __exit__() -> Context manager (with)

# __eq__(), __It__(), etc - Comparison

