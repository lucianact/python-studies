# suppose we already have a node class and a linked list class
class Node(object):
    """A node in a linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    """A singly linked list."""

    def __init__(self, head=None):
        self.head = None

# and we also have a linked list implemented
say_hi = SinglyLinkedList()
first_node = Node("hello")
second_node = Node("world")
third_node = Node("!")
say_hi.head = first_node
first_node.next = second_node
second_node.next = third_node

# now design certain functions outside the liked list class:
# (meaning function that are not methods)
def print_linked_list(head_node): 
    """Print a linked list."""
    
    # check if the linked list is empty:
    if head_node is None:
        return "Linked list is empty!"

    current_node = head_node
    while current_node:
        print(current_node.data)
        current_node = current_node.next 

print_linked_list(first_node)
# note that you don't need to necessarily print the whole list, 
# you can pass the second_node as an argument, for example

def find_value(head_node, value):
    """Find node/value in a linked list."""

    # check if the linked list is empty:
    if head_node is None:
        return "Linked list is empty!"

    current_node = head_node
    while current_node:
        if current_node.data == value:
            return True 
        current_node = current_node.next  
    return False   

print(find_value(first_node, "world"))

def reassign_node(head_node, current_value, new_value):
    """Reassign target node a new value."""

    # check if the linked list is empty:
    if head_node is None:
        return "Linked list is empty!"

    current_node = first_node
    while current_node:
        if current_node.data == current_value:
            current_node.data = new_value
            return 
        current_node = current_node.next
    return "Node couldn't not be found"

print(reassign_node(first_node, "world", "universe"))
print_linked_list(first_node) 

def find_the_length(head_node):
    """Find linked list length."""

    # check if the linked list is empty:
    if head_node is None:
        return "Linked list is empty!"

    current_node = first_node
    lllength = 0  
    while current_node:
        lllength += 1 
        current_node = current_node.next
    return lllength

print(find_the_length(first_node))

def prepend_node(head_node, new_node):
    """Prepend a new node to a linked list."""

    # create new node
    new_node = Node(new_node)

    # check if the linked list is empty:
    if head_node is None:
        head_node = new_node
        
    new_node.next = head_node
    head_node = new_node
    return head_node.data

print(prepend_node(first_node, "Say:"))
# what happens now if we print these following functions? 
print_linked_list(first_node)
print(find_the_length(first_node)) # what do I do now if I want to print the new length?

def append_node(head_node, new_node):
    """Append new node to linked list."""

    # create new node
    new_node = Node(new_node)

    # check if linked list is empty
    if head_node is None:
        head_node = new_node
        
    current_node = head_node
    while current_node.next:
        current_node = current_node.next
    current_node.next = new_node

print(append_node(first_node, "!"))
print_linked_list(first_node) 

def insert_a_node_after_target_node(head_node, target_value, new_node):
    """Inser a new node after target node."""

    # create new node
    new_node = Node(new_node)

    # check if linked list is empty
    if head_node is None:
        return "Linked list is empty!"

    current_node = head_node
    while current_node:
        if current_node.data == target_value:
            new_node.next = current_node.next
            current_node.next = new_node
        current_node = current_node.next

    return "Node could not be found"  

insert_a_node_after_target_node(first_node, "universe" , "of love")
print_linked_list(first_node)

def insert_a_node_before_target_node(head_node, target_value, new_node):
    """Insert a new node before a target node."""

    # create new node
    new_node = Node(new_node)

    # check if list is empty:
    if head_node is None:
        return "Linked list is empty!"
    
    # check if head is the target value
    if head_node.data == target_value:
        new_node.next = head_node
        head_node = new_node
        return

    current_node = head_node
    while current_node.next:
        if current_node.next.data == target_value:
            new_node.next = current_node.next
            current_node.next = new_node
            return
        current_node = current_node.next  

insert_a_node_before_target_node(first_node, "universe", "beautiful")
print_linked_list(first_node)

def remove_a_node(head_node, value_to_be_removed):
    
    # check if we have an empty linked list:
    if head_node is None:
        raise Exception("List is empty!")

    # check if the node to be removed
    # is the head node:
    if head_node.data == value_to_be_removed:
        head_node = head_node.next 

    current_node = head_node 
    while current_node.next:
        if current_node.next.data == value_to_be_removed:
            current_node.next = current_node.next.next 
        current_node = current_node.next 
    
    return "Node could not be found!"

remove_a_node(first_node, "beautiful")
print_linked_list(first_node)