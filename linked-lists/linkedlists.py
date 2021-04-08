class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = None
    
    def prepend_node_method(self, new_node):
        new_node = Node(new_node)
        head_node = new_node
        head_node.next = self.head 
        return head_node.data
    
    def append_node_method(self, new_node):
        new_node = Node(new_node)
        current_node = self.head
        while current_node:
            current_node = current_node.next
        current_node = new_node
        return current_node.data
    
    def print_linked_list_method(self): 
        current_node = self.head 
        while current_node:
            print(current_node.data)
            current_node = current_node.next 
    
    def find_value_method(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                # return f'{current_node} is {value}'
                return True 
            current_node = current_node.next    
    
    def reassign_node_value_method(self, current_value, new_value):
        current_node = self.head
        while current_node:
            if current_node.data == current_value:
                current_node.data = new_value
                return current_node.data
            current_node = current_node.next    
    
    def find_the_length_method(self):
        current_node = self.head
        lllength = 0 
        while current_node:
            lllength += 1 
            current_node = current_node.next   
        return lllength
    
    def insert_a_node_after_target_node_method(self, target_node_value, new_node):
        new_node = Node(new_node)
        current_node = self.head
        while current_node:
            if current_node.data == target_node_value:
                new_node.next = current_node.next
                current_node.next = new_node
            current_node = current_node.next
    
    # def insert_a_node_before_target_node_method(self, target_node_value, new_node):
    #     new_node = Node(new_node)
    #     current_node = self.head
    #     while current_node:
    #         if current_node.data == target_node_value:
    #             new_node.next = current_node
    #             current_node.next = new_node
    #         current_node = current_node.next  
    # Reminder that something is wrong here!

    def remove_a_node(self, to_be_removed):
        
        # check if we have an empty linked list:
        if self.head is None:
            raise Exception("List is empty!")

        # check if the node to be removed
        # is the head node:
        if self.head.data == to_be_removed:
            self.head = self.head.next 
        
        # otherwise:
        current_node = self.head 
        while current_node.next:
            if current_node.next.data == to_be_removed:
                current_node.next = current_node.next.next 
            current_node = current_node.next 
            


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

#     def __repr__(self):
#         return f"Node is {self.data}, next node is {self.next.data}" if self.next else None

say_hi = SinglyLinkedList()
first_node = Node("hello")
second_node = Node("world")
third_node = Node("!")
say_hi.head = first_node
first_node.next = second_node
second_node.next = third_node

# ??? why this doesn't work ????
# third_node = Node("!")
# second_node = Node("world", third_node)
# first_node = Node("hello", second_node)
# say_hi = SinglyLinkedList(first_node)

def print_linked_list_function(head_node): 
    current_node = head_node
    while current_node:
        print(current_node.data)
        current_node = current_node.next 
print_linked_list_function(first_node)
# you don't need to necessarily print the whole list 
# you can pass the second_node as an argument, for example

def find_value_function(head_node, value):
    current_node = head_node
    while current_node:
        if current_node.data == value:
            # return f'{current_node} is {value}'
            return True 
        current_node = current_node.next    
# print(find_value_function(first_node, "world"))

def reassign_node_value_function(first_node, current_value, new_value):
    current_node = first_node
    while current_node:
        if current_node.data == current_value:
            current_node.data = new_value
            return current_node.data
        current_node = current_node.next 
# print(reassign_node_value_function(first_node, "world", "universe"))
# what happens now if we print this following function? 
# print_linked_list_function(first_node) 

def find_the_length_function(first_node):
    current_node = first_node
    lllength = 0  
    while current_node:
        lllength += 1 
        current_node = current_node.next
    return lllength
# print(find_the_length_function(first_node))

def prepend_node_function(first_node, new_node):
    new_node = Node(new_node)
    head_node = new_node
    head_node.next = first_node
    return head_node.data
# print(prepend_node_function(first_node, "Say:"))
# what happens now if we print these following functions? 
# print_linked_list_function(first_node)
# print(find_the_length_function(first_node)) # why?

def append_node_function(first_node, new_node):
    new_node = Node(new_node)
    current_node = first_node
    while current_node:
        current_node = current_node.next
    current_node = new_node
    return current_node.data
# print(append_node_function(first_node, "!"))
# print_linked_list_function(first_node) # why?

def insert_a_node_after_target_node_function(first_node, target_node_value, new_node):
    new_node = Node(new_node)
    current_node = first_node
    while current_node:
        if current_node.data == target_node_value:
            new_node.next = current_node.next
            current_node.next = new_node
        current_node = current_node.next  
        # return f'{current_node.next.data}' # what's happening? 
# insert_a_node_before_target_node_function(first_node, "world" , "of love")
# print_linked_list_function(first_node)

# def insert_a_node_before_target_node_function(first_node, target_node_value, new_node):
#     new_node = Node(new_node)
#     current_node = first_node
#     while current_node:
#         if current_node.data == target_node_value:
#             new_node.next = current_node
#             current_node.next = new_node
#             break
#         current_node = current_node.next  
# insert_a_node_before_target_node_function(first_node, "world", "beautiful")
# print_linked_list_function(first_node)


# class NoTailLinkedList(object):
#     """Linked List using head only."""
    
#     def __init__(self):
#         self.head = None
    
#     def append_node(self, data):
#         """Append node with data to end of list."""

#         # creating a node inside the method 
#         new_node = Node(data)

#         # should the new node be the head of our ll?
#         if self.head is None:
#             self.head = new_node
#         # the last node of the ll will always point to none
#         else:
#             current_node = self.head
#             while current_node.next is not None:
#                 current_node = current_node.next
#             current_node.next = new_node
    
#     def print_list(self):
#         """Print all items in the list."""

#         current_node = self.head

#         while current_node is not None:
#             print(current_node.data)
#             current_node = current_node.next 


# class LinkedList(object):
#     """Linked List using head and tail."""
    
#     def __init__(self):
#         self.head = None
#         self.tail = None
        
#     def append(self, data):
#         """Append node with data to the end of the list."""

#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
        
#         if self.tail is not None:
#             self.tail.next = new_node
        
#         # while the ll is empty:
#         self.tail = new_node
    
#     def print_list(self):
#         """Print all items in the list."""

#         current = self.head

#         while current is not None:
#             print(current.data)
#             current = current.next

#     def find(self, data):
#         """Does this data exist in our list?"""

#         current = self.head

#         while current is not None:
#             if current.data == data:
#                 return True
#             current = current.next
#         return False
    
#     def remove(self, value):
#         """Remove node with given value"""

#         # If removing head, make 2nd item (if any) the new .head
#         if self.head is not None and self.head.data == value:
#             self.head = self.head.next
#             if self.head is None:
#                 self.tail = None
#             return

#         # Removing something other than head
#         current = self.head

#         while current.next is not None:

#             if current.next.data == value:
#                 current.next = current.next.next
#                 if current.next is None:
#                     # If removing last item, update .tail
#                     self.tail = current
#                 return

#             else:     # haven't found yet, keep traversing
#                 current = current.next



