# How could you reverse a Linked List if all of you know is it's head node?
class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

# Always think about the edge cases:
# What if this Linked List has only one node?
# What if this Linked List is empty? 

# Return the "new" head of that Linked List: 
def reverse(head_of_list):
    
    # When I think about a reversed  Linked List, 
    # there's two first things that jump in my head right away:
    # the head node will beacome the tail node 
    # and the tail node will become the head node.
    # Alright!
    # What about the "in between" nodes?
    
    # Visualization
    # Let's suppose we have this Linked List:
    # A -> B -> C -> D 
    # And we want this out come:
    # D -> C -> B -> A
    # How you could make that happen?
    
    # So let's start travesing this Linked List until get to its last node!

    # What if we keep track of the node we've just visited
    # with a .previous pointer?
    # Because in the end, this .previous pointer will be our .next!
    # But before we traverse this list,
    # our current_node is head_of_list and 
    # the previous_node is None.
    current_node = head_of_list
    previous_node = None 
    
    if current_node is None:
        return None 
  
    while current_node.next:
        previous_node = current_node     # after reversing will be next 
        current_node = current_node.next # will become head 
        
    
    # Now we can imagine that our node head will be the last node:
    head_of_list = current_node 
    print(head_of_list)
    return head_of_list
    
    # But we still haven't node anything for the "in between" numbers!
    

    # We also know that the previous node, should become the .next node:
    head_of_list.next = previous_node 
    
    # How can we automate this backward process?