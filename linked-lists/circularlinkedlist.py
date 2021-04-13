class Node(object):
    """A node in a linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    """A circular linked list."""

    def __init__(self, head=None):
        self.head = None

    def prepend_node(self, new_node):
        """Prepend a new node to a circular linked list.""" 

        # create a new node:
        new_node = Node(new_node)

        # check if list empty:
        if self.head is None:
            self.head = new_node
            new_node.next = new_node

        # when we have a perfect circular linked list,
        # the last node instead of poiting to None, 
        # now poitns back to the head node. 

        # so when we add a new head to our linked list, 
        # besides updating the head node and the current 
        # .next head node pointer, we also need to 
        # update the last node .next pointer:
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head
    

    def append_node(self, new_node):
        """Append a new node to a circular linked list."""
        
        # create a new node:
        new_node = Node(new_node)
        
        # check if list is empty:
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        
        # else:
        # when we add a new head to our linked list, 
        # besides updating the head node and the current 
        # .next head node pointer, we also need to 
        # update the last node .next pointer:
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head 
        
    
    def print_linked_list(self): 
        """Print a circular linked list."""
        
        # check if list is empty:
        if self.head is None:
            raise Exception("List is empty!")
        
        # check if list has only one node:
        if ((self.head.next == self.head) or 
                (self.head.next == None)):
            print(self.head.data)

        # else:
        current_node = self.head
        while current_node.next != self.head:
            print(current_node.data)
            current_node = current_node.next