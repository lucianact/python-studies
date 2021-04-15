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