# Queues:
# first in, first out
# you add items by enqueueing them at the back (end)
# you remove items by dequeueing them at the front
# thus, newer items are in the end!
# 
# Methods: 
# enqueue(item)
# dequeue()
# peek() 
# is_empty()


# Implementations (simple implementation versions):
# using a list
data = []
data.append(5)                      # enqueue()
print(data[0])                      # peek()
data.pop(0)                         # dequeue()
if data == []:
    print("queue is empty")         # is_empty()

# using the deque library
from collections import deque
data1 = deque()
data1.append("Luci")
data1.append("Nico")
element = data1.popleft()
print(element, data1)

# building a class
class Queue(object):
    """A simple queue, implemented using a list."""

    def __init__(self):
        self._data = []

    def enqueue(self, item):
        """Add to end of queue."""
        self._data.append(item)

    def dequeue(self):
        """Remove from front of queue."""
        return self._data.pop(0)

    def peek(self):
        """Show first item in queue."""
        return self._data[0]

    def is_empty(self):
        """Is queue empty?"""
        return not self._data

# Stacks:
# last in, first out
# you add items by pushing them onto the top
# you remove items by poping them off the front
# thus, newer item are near the top of the stack
# 
# Methods: 
# push(item)
# pop()
# peek()
# is_empty()

# Implementations (simple implementation versions):
# using a list
data2 = []
data2.append(5)                      # push()
print(data2[-1])                     # peek()
data2.pop()                          # pop()
if data2 == []:
    print("stack is empty")         # is_empty()

# using the deque library
from collections import deque
data3 = deque()
data3.append("Luci")
data3.append("Nico")
element = data3.pop()
print(element, data3)

# building a class
class Stack(object):
    """A simple Stack, implemented using a list."""

    def __init__(self):
        self._stack = []

    def push(self, item):
        """Add item to top."""
        self._stack.append(item)

    def pop(self):
        """Remove top item."""
        return self._stack.pop()

    def peek(self):
        """Return, but don't remove, top item."""
        return self._stack[-1] # if not len(self._stack) else None

    def is_empty(self):
        """Is the stack empty?"""
        return not self._stack # return not len(self._stack)


# OBS:
# Stacks & Queues are a restrict ordered collection of data
# (they're like a specialized list that do what they need to do)
 

