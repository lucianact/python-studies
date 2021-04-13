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

# My head's first approach:
# 
# how do you delete a node from a linked list? 
#
# 1st:
# traverse the list looking for the node which 
# carries the value to be deleted. 
# 
# # 3rd:
# when we do find the target node, we need to:
# twich the .next poiter from the node that comes before he target node
# to point to the node that comes after the targed node
# 
# 2nd:
# before doing that, there are some edge cases we could face here:
# -> linked list might be empty 
# -> this specific node might not be in the linked list
# -> the target node might the head of the list

# But what if :
#
# 1. we are not talking about the value of the node, but the node itself
# 2. we don't have access to the head node nor to the previous node?
# 
# New approach:
# 
# twitching the previous node pointer would be complicade in this case, 
# but we can still reassign the node to be deleted to be the next node
# and twich the .next pointer to skip from the .next node,
# to the node which comes after.
#
# I would personally still "secure" for possible edge cases anyway,
# when twitching the pointers around:
# -> what if we don't find the node?
# -> what happens if we're deleting the last node?

def delete_a_node(node_to_delete):

    curent_node = node_to_delete
    next_node = curent_node.next 

    if next_node:
        curent_node.value = next_node.value
        curent_node.next = next_node.next 
    else:
        raise Exception("Error was found for this type of solution!")

"""
There are two potential side-effects:

Any references to the input node have now effectively been reassigned 
to its next node. In our example, we "deleted" the node assigned to the
variable b, but in actuality we just gave it a new value (2) and a new next! 
If we had another pointer to b somewhere else in our code and 
we were assuming it still had its old value (8), that could cause bugs.

If there are pointers to the input node's original next node,
those pointers now point to a "dangling" node (a node that's no longer 
reachable by walking down our list). In our example above, c is now dangling. 
If we changed c, we'd never encounter that new value 
by walking down our list from the head to the tail.

Complexity
O(1) time and O(1) space.

What we wearned?
My favorite part of this problem is how imperfect the solution is. 
Because it modifies the list "in place" it can cause other parts of 
the surrounding system to break. This is called a "side effect."
In-place operations like this can save time and/or space, but they're risky.
If you ever make in-place modifications in an interview, 
make sure you tell your interviewer that in a real system you'd 
carefully check for side effects in the rest of the code base.

"""


    



  



