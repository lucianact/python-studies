"""

Delete a node from a singly-linked list, 
given only a variable pointing to that node.

"""

class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
a.next = b
b.next = c
