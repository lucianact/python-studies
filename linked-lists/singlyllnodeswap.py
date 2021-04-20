"""
Swap nodes in a linked list without swapping data.

Given a linked list and two keys in it, swap nodes for two given keys. 
Nodes should be swapped by changing links. 

It may be assumed that all keys in the linked list are distinct.

-> x and y may or may not be adjacent. 
-> Either x or y may be a head node. 
-> Either x or y may be the last node. 
-> x and/or y may not be present in the linked list.
"""

class LinkedList(object):
    def __init__(self):
        self.head = None
 
    # head of list
class Node(object):
    def __init__(self, d):
        self.data = d
        self.next = None

# The idea is to first search x and y in the given linked list. 
# If any of them is not present, then return. 
# While searching for x and y, 
# keep track of current and previous pointers. 
# First change next of previous pointers, 
# then change next of current pointers. 

def swap_node(self, value_one, value_two):

    # Nothing to do if x and y are same
    if value_one == value_two:
        return "Values cannot be the same"

    current_one = self.head
    previous_one = None 

    current_two = self.head
    previous_two = None

    while current_one.data != value_one:
        previous_one: current_one
        current_one = current_one.next
        if current_one is None:
            return "Value could not be found"
    # now current_one is value_one

    while current_two.data != value_one:
        previous_two: current_two
        current_two = current_two.next
        if current_two is None:
            return "Value could not be found"
    # now current_two is value_two

    # suppose we have:
    # current_one = B
    # previous_one = A
    # current_two = C
    # previous_two = B
    # A -> B -> C -> D

    # A -> C
    previous_one.next = current_two
    # C -> B
    current_two.next = previous_two
    # now we have: A -> C -> B 
    # but B still poiting to C:
    previous_two.next = current_two.next