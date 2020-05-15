# In Python, any data will be stored as an object.
# An object has 3 types - id, type, value
# Explained well in this article - https://medium.com/datadriveninvestor/mutable-and-immutable-python-2093deeac8d9
#####################################

# ID 

# Memory location (ID)
a = 1
# to check the unique id of the object
# location in memory
print(id(a))

# to understand the concept of Id
a = 1
print(id(a))

b = 2
print(id(2))

# check whether a and b are having same id
print(id(a)==id(b)) # False

# now give the same value for c as in b
c = 2
print(id(c))

# now b and c should be equal
# as they both contain the value 2
# hence will be pointed to same location in memory
print(id(b)==id(c)) # True


# id can be used for multiple types
# Ex: for Strings
name1 = "loki"
name2 = "loki"
print(id(name1)==id(name2)) # True

# change the name1 to caps L
name1 = "Loki"
name2 = "loki"
print(id(name1)==id(name2)) # False


# Tricky with int 
d = 256
e = 256
print(id(d)==id(e)) # True

f = 260
g = 260
print(id(f)==id(g)) # False

# why 256 returned True and 260 returned False?
# Python - keeps array of integer objects between -5 and 256. 
# so when we create in the above range, we get reference to the already existing object
# does this with 2 macros - NSMALLNEGINTS, NSMALLPOSINTS

# For lists, we can check using "IS"
# is helps to check if 2 variables have the same object ID
list1 = [1,2,3]
list2 = list1
print(list1 is list2) # True

# ALIASING:
# which means list2 is just an alias of list1 - aliasing?
# variables refer to objects and if we assign one variable to another, both variables will refer to same object

# CLONING:
# If we want to modify a list and also keep a copy of original list, we need to copy it
# this process is cloning
# slicing a list, creates a new list
list3 = [1,2,3]
list4 = list3[:] # creating list using slicing
print(list4 is list3) #False, because slicing a list creates a new list
print(id(list3)==id(list4)) # False, as its new list, it will have its own memory location
####################################

# TYPE
# will provide the type of the object that's passed in the argument

print(type(2)) # <class 'int'>
print(type(-6.25)) # <class 'float'>
print(type(2,)) # <class 'tuple'>
print(type("hello")) # <class 'str'>
print(type('346.788')) # <class 'str'>
print(type([2,3,4])) # <class 'list'>
print(type({'category':'produce', 'count':200})) # <class 'dict'>
print(type(type)) # <class 'type'>
print(type(print)) # <class 'builtin_function_or_method'>

####################################

# Mutable Objects
# list, dict, set

# program stores data in variables that represent storage locations in the computer's memory
# contents of memory locations, at any given point in the program's execution, is called program's state
# since objects in python are mutable, some are immutable
# mutable object - changeable object and its state can be modified after it is created

my_list = ['cat','dog','bunny']
print(my_list)
print(id(my_list))

# change the first value of the list
# but memory address of the list is same
my_list[0] = 'sugar glider'
print(my_list)
print(id(my_list))

# when we modify a list and change its value in place, the list keeps the same address
# id of the list will be same, 
# however id of the list element will be different


#####################################
# Immutable Objects
# integer, float, string, tuple, bool, frozenset

# is an object that is not changeable and its state cannot be modified after it is created
# string is immutable, cannot overwrite the values of immutable objects
phrase = "how you like me now"
print(phrase)
print(id(phrase))
phrase = "do you fee lucky?"
print(phrase)
print(id(phrase))

# since a string is immutable, it creates a new string object
# memory addresses do not match
print(phase[0]='D')
# TypeError: 'str' object does not support item assignment
# TypeError because strings are immutable.
# We can't change the string object


#####################################
# Why do mutable and immutable objects matter?
# Immutability may be used to ensure that an object remains constant throughout your program.
# The values of mutable objects can be changed at any time and place, whether you expect it or not

####################################
# Strings - slicing, concatenation, character-wise, access using index, strip

str = 'Hello World!'

# print complete string
print(str)

# print first character of the string
print(str[0])

# print characters starting from 3rd to 5th
print(str[2:5])

# print string starting from 3rd character
print(str[2:])

# print string 2 times
print(str * 2)

# print concatenated string
print(str + "test")
