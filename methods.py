# In python "Methods" usually refer to functions that are associated with objects, 
# expecially class instances or built-in types like str, list, dist etc

# Includes Built-in data types, special methods and common objects via OOP

# * ~~ String Methods ~~

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
# a.intersection(b)

# difference()
# a.difference(b)