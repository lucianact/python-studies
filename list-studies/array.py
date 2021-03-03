# Array:
# an array organizes item sequentially
# (one after the other in memory)
# which makes them cache-friendly
#
# each position in the array has an index
# the index starts at position 0

# Strenghts:
# 1. fast lookup:
# retrivieng an element at given index has 0(1) time
#
# 2. fast appends:
# adding a new element at the end of an array taks 0(1) time
# (if the array has the space)

# Weaknesses:
# 1. fixed size (not in Python):
# unless you're using a dynamic array, you have to specify
# how many elements you're going to store in the the array
# ahead of time
#
# 2. Costly inserts and deletes:
# you have to "scoot over" the other elements to fill in or
# close gaps, which will take worst-case O(n) time.

# Why we need to scoot over even when deleting an element
# instead of leavinf an gap?
# 
# -> the quick lookup power of arrays depends on everything 
# being sequential and uninterrupted.
# -> otherwise we cannot predict how far form the start of the array
# and nth item is / where each item will be (like a linked list)

# Array slicing:
# involves taking a subset from an array
# and allocating a new array with those elements

# example in pythin 3.6:
my_list = ["a", "b", "c", "d"]
new_subset_list = my_list[1:3] # my_list[start_index:end_index]

# You can also get everything from start_index onwards 
# by just omitting end_index:
new_subset_list = my_list[1:] # my_list[start_index:]

# There's a hidden time and space cost here!
# but in reality you are:
# 1. allocating a new list
# 2. copying the elements from the original list to the new list
# This takes O(n) time and O(n) space
# where n is the number of elements in the resulting list.

# Dynamic Array (list in Python)
# is an array waith a bid  improvement:
# automatic resizing

# Strengths:
# 1. fast lookups:
# just like arrays, retrieving the element at a given index takes O(1) time.
# 2. variable size:
# you can add as many items as you want, and the dynamic array will expand to hold them.
# 3. cache-friendly:
# just like arrays, dynamic arrays place items right next to each other in memory,
#  making efficient use of caches.

# Weaknesses:
# 1. slow worst-case appends:
# usually, adding a new element at the end of the dynamic array takes O(1) time. 
# but if the dynamic array doesn't have any room for the new item, it'll need to expand, which takes O(n) time.
# 2. costly inserts and deletes:
# just like arrays, elements are stored adjacent to each other. 
# so adding or removing an item in the middle of the array requires "scooting over" other elements, which takes O(n) time.

# List in Python
# ordered, mutable collection of items
# and it can be heterogenous collection of items
animals = ['aardvark', 'bear', 'cow']

# length of a list:
animals = ['aardvark', 'bear', 'cow']
len(animals)    # => 3

# check for item:
'cow' in animals    # => True
'deer' in animals   # => False

# count how many times an item appears in a list:
animals.count('cow')   # => 1
animals.count('deer')  # => 0

# get item from List
animals[1]     # => 'bear'
animals[-1]    # => 'cow'
animals[-2]    # => 'bear'

animals[1] = "baboon"
animals        # => ['aardvark', 'baboon', 'cow']

# unpacking lists:
animals = ['aardvark', 'bear', 'cow']
a1, a2, a3 = animals

# add items to list
animals.append('deer')
animals.append('eagle')
animals.extend(['frog', 'gerbil'])
animals.append(['frog', 'gerbil'])
animals.extend('hamster')

# removing items
animals = ['aardvark', 'bear', 'cow']

animals.pop()    # => 'cow'
animals          # => ['aardvark', 'bear']

animals.pop(0)   # => 'aardvark'
animals          # => ['bear']

del animals[0]
animals          # => []  

# you can also remove the first incidence of 
# a particular value with:
animals.remove('cow')
# which removes the first cow from the list

# sorting
# list.sort() sorts in-place:
animals = ['aardvark', 'cow', 'bear']
animals.sort()    # returns None!
animals    # => ['aardvark', 'bear', 'cow']

# sorted(list) returns new sorted list:
animals = ['aardvark', 'cow', 'bear']
sorted(animals)    # => ['aardvark', 'bear', 'cow']
animals    # => ['aardvark', 'cow', 'bear']

# There’s an analogous set for reversing a list: 
# list.reverse() reverses a list in place, whereas
#  reversed(list) returns a new sorted list.

# (Actually, reversed(list) returns a “generator object”
# of your reversed list. 
# This is an object that is “lazy” — 
# that is, rather than having to create an
#  entirely new list of yours, reversed, 
# you get this object you can iterate over that 
# can give you the “next” item sequentially as 
# you ask for it.)

# list slicing
# list[start:stop]
# start is included, stop is excluded
nums = [10, 20, 30, 40, 50, 60]
nums[3:5]
# => [40, 50]
nums[3:]
# => [40, 50, 60]
nums[:2]
# => [10, 20]

# list[start:stop:step]
nums = [10, 20, 30, 40, 50, 60]
nums[0:4:2]
# => [10, 30]
nums[::2]
# => [10, 30, 50]

# it’s an error to index a nonexistent item:
nums[99]    # => IndexError

# it’s not an error to slice to an empty list:
nums[99:]   # => []

# negative start or stop refer to end of list:
nums = [10, 20, 30, 40, 50, 60]
#       -6  -5  -4  -3  -2  -1
nums[-2:]
# => [50, 60]
nums[:-2]
#  => [10, 20, 30, 40]

# negative step goes backwards:
nums = [10, 20, 30, 40, 50, 60]
#       -6  -5  -4  -3  -2  -1
nums[3:1:-1]
# => [40, 30]
nums[::-1]
# => [60, 50, 40, 30, 20, 10]

# you can assign to a list slice, too
animals = ['aardvark', 'bear', 'cow']
animals[1:3] = ['moose']
# => ['aardvark', 'moose']

animals = ['aardvark', 'bear', 'cow', 'deer']
animals[1:-1] = []
# => ['aardvark', 'deer']

# iteration is over objects:
yay = ['kittens', 'tea', 'tiny ice cream cones']
for adorable in yay:
    print("I love", adorable)

#    for (i = 0; i < yay.length; i = i + 1) {
#   // refer to the "current" item as yay[i]
# }

# you don’t loop over numbers directly:
# for number in 5:
#     print(number, "is my favorite number")
# TypeError: 'int' object is not iterable

# range
for number in range(5):
    print(number, "is my favorite number")

# range(stop) constructs an iterable range object:
range(5)        # => range(0, 5)
list(range(5))  # => [0, 1, 2, 3, 4]

# range(start, stop, step)
# like list slicing, doesn’t include stop:
list(range(2, 8))       # => [2, 3, 4, 5, 6, 7]
list(range(2, 8, 2))    # => [2, 4, 6]
list(range(5, 0, -1))   # => [5, 4, 3, 2, 1]

# when looping, sometimes you just care about items:
fruits = ['apple', 'berry', 'cherry']

for fruit in fruits:
    print(fruit)
    # => apple
    # => berry
    # => cherry

# sometimes, you need the index of the item, too:
for i in range(len(fruits)):
    print("fruit {} is {}".format(i, fruits[i]))
    # => fruit #0 is apple
    # => fruit #1 is berry
    # => fruit #2 is cherry