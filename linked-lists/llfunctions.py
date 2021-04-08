class Node(object):
    """A node in a linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    """A singly linked list."""

    def __init__(self, head=None):
        self.head = None

say_hi = SinglyLinkedList()
first_node = Node("hello")
second_node = Node("world")
third_node = Node("!")
say_hi.head = first_node
first_node.next = second_node
second_node.next = third_node

def print_linked_list(head_node): 
    current_node = head_node
    while current_node:
        print(current_node.data)
        current_node = current_node.next 
print_linked_list(first_node)
# you don't need to necessarily print the whole list 
# you can pass the second_node as an argument, for example

def find_value_function(head_node, value):
    current_node = head_node
    while current_node:
        if current_node.data == value:
            return True 
        current_node = current_node.next  
    return False   
print(find_value_function(first_node, "world"))

def reassign_node(head_node, current_value, new_value):
    current_node = first_node
    while current_node:
        if current_node.data == current_value:
            current_node.data = new_value
            return current_node.data
        current_node = current_node.next 
print(reassign_node(first_node, "world", "universe"))
# what happens now if we print this following function? 
print_linked_list(first_node) 

def find_the_length(head_node):
    current_node = first_node
    lllength = 0  
    while current_node:
        lllength += 1 
        current_node = current_node.next
    return lllength
print(find_the_length(first_node))

def prepend_node(head_node, new_node):
    new_node = Node(new_node)
    head_node = new_node
    head_node.next = first_node
    return head_node.data
print(prepend_node(first_node, "Say:"))
# what happens now if we print these following functions? 
print_linked_list(first_node)
print(find_the_length(first_node)) # why?

def append_node(head_node, new_node):
    new_node = Node(new_node)
    current_node = first_node
    while current_node:
        current_node = current_node.next
    current_node = new_node
    return current_node.data
print(append_node(first_node, "!"))
print_linked_list(first_node) # why?

def insert_a_node_after_target_node(head_node, target_node_value, new_node):
    new_node = Node(new_node)
    current_node = first_node
    while current_node:
        if current_node.data == target_node_value:
            new_node.next = current_node.next
            current_node.next = new_node
        current_node = current_node.next  
insert_a_node_after_target_node(first_node, "world" , "of love")
print_linked_list(first_node)

def insert_a_node_before_target(head_node, target_node_value, new_node):
    new_node = Node(new_node)
    current_node = first_node
    while current_node.next:
        if current_node.next.data == target_node_value:
            new_node.next = current_node.next
            current_node.next = new_node
            return
        current_node = current_node.next  
insert_a_node_before_target(first_node, "world", "beautiful")
print_linked_list(first_node)

