"""

Hooray! It's opposite day. Linked lists go the opposite way today.

Write a function for reversing a linked list. Do it in place. 

Your function will have one input: the head of the list.

Your function should return the new head of the list.

"""

# clarification notes to self:
#
# to reverse a linked list in place
# you need to twitch a few pointer as you traverse
#
# starting from the head node, the head_node.next
# pointer should now point to None, to became the last node
# of the linked list.
# 
# but before we reassign pointers, we need to "save" its
# current reference to be the .next node of the head_node.next node
# 
# meaning that we need to keep track of the previous node
# before we reassign this node to be something else
#
# so as we traverse the linked list, the previous_node should
# "jump" to the next node


class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

def reverse(head_of_list):
    """Reverse a linked list in place."""

    # ! edge cases first ! 
    if head_of_list is None:
        # raise Exception("Linked list is empty!")
        return None
    
    if head_of_list.next is None:
        # raise Exception("Linked list has only one node!")
        return head_of_list

    # else:

    current_node = head_of_list
    previous_node = None

    # as we move forward
    #     (
    #       how do we move foward? 
    #       -> iterating throught our linked listL
    #       meaning that we move foward as long as current_node.next is True
    #      )
    # our previous_node also move forward 
    
    # the current_node will now be pointing to the previous node:
    # meaning current_node.next will be the previous_node
    # and the current_node.next will be now pointing to the current_node

    while current_node.next:
        current_node.next = previous_node
        previous_node = current_node
        current_node = current_node.next 
        return previous_node

# WHY? 