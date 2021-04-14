"""

You have a linked list and want to find the nth to last node.

Write a function kth_to_last_node() that takes an integer k 
and the head_node of a singly-linked list,
and returns the kkth to last node in the list.

"""

class LinkedListNode:
    
    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# Returns the node with value "Devil's Food" (the 2nd to last node)
# nth_to_last_node(2, a)

def nth_to_last_node(nth, head_node):

    # to keep track of a the nth to the last node
    # it's necessary to know the whole linked list;
    # meaning that it's necessary to traverse the ll

    # we find the lenght by creating a varible to 
    # keep track of how many nodes we have visited
    # until we reach None

    # To make time complextiy better, instead of 
    # traversing the ll twice, we can also create
    # a variable to keep track of the order of
    # the nodes visited, making easiar (faster)
    # to return the nth to the last node

    # first check if ll is empty:
    if head_node is None:
        return None 
    
    current_node = head_node
    length = 0
    nodes_seen = []

    while current_node:
        length += 1
        nodes_seen.append(current_node)
        current_node = current_node.next 
    
    print(length)
    print(nodes_seen)

    if nth >= length:
        return None
    else:
        the_nth_node = nodes_seen[-nth].value
        print(the_nth_node)
        return the_nth_node

nth_to_last_node(2, a)