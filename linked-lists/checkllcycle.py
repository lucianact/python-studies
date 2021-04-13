"""
You have a singly-linked list and want to check if it contains a cycle.

A singly-linked list is built with nodes, where each node has:
node.next—the next node in the list.
node.value—the data held in the node. 

For example:
if our linked list stores people in line at the movies, 
node.value might be the person's name.

A cycle occurs when a node’s next points back to a previous node in the list.
The linked list is no longer linear with a beginning and end—instead, 
it cycles through a loop of nodes.

Write a function contains_cycle() that takes the first node in a singly-linked
list and returns a boolean indicating whether the list contains a cycle.

"""

class LinkedListNode(object):
    """A linked list node."""

def __init__(self, value):
    self.value = value
    self.next  = None

# At first, my approach would be to traverse this linked list
# and as I traverse, I check if any .next node pointer is pointing
# back to a node I have alredy visited. 
#
# I do know that traversing a whole linked list will cost me O(n) time, 
# but I also need to keep in mind that the last node can also point back
# to a node already viside - making the traversion necessary.
#
# To make sure if my linked list is circular, I need to find a way
# to store every node visited. How could I do that? 
# Using a set in this case seems smart, since we a set 
# will not allow repetition of data.
#
# Let's organize the algorithm:
# -> If the current node is already in our set, we have a cycle. Return True.
# -> If the current node is None we've hit the end of the list. Return False.
# -> Else throw the current node in our set and keep going.

def contains_cycle(head_node):
    """Check if linked list is circular."""

    # check if the list is empty:
    if head_node is None:
        # raise Exception("List is empty!")
        return False
    
    # else:
    visited_nodes = set()
    current_node = head_node
    while current_node.next:
        if current_node in visited_nodes:
            return True
        visited_nodes.add(current_node)
        current_node = current_node.next
    return False 

# def contains_cycle(first_node):
#     # Start both runners at the beginning
#     slow_runner = first_node
#     fast_runner = first_node

#     # Until we hit the end of the list
#     while fast_runner is not None and fast_runner.next is not None:
#         slow_runner = slow_runner.next
#         fast_runner = fast_runner.next.next

#         # Case: fast_runner is about to "lap" slow_runner
#         if fast_runner is slow_runner:
#             return True

#     # Case: fast_runner hit the end of the list
#     return False