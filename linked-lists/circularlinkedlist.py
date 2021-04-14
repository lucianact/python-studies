class Node(object):
    """A node in a linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    """A circular linked list."""

    def __init__(self, head=None):
        self.head = None

    def append_node(self, new_node):
        """Append a new node to a circular linked list.""" 

        # create a new node:
        new_node = Node(new_node)

        # check if list empty:
        if self.head is None:
            self.head = new_node
            new_node.next = new_node

        # when we have a perfect circular linked list,
        # the last node instead of poiting to None, 
        # now poitns back to the head node. 

        # so when we append a new node to our linked list, 
        # we also need to update the last node .next pointer
        # to point to the new node and the new node .next
        # pointer should now point to the node head
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head
    

    def prepend_node(self, new_node):
        """Prepend a new node to a circular linked list."""
        
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
        self.head = new_node
        
    
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
        while current_node.next:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break 
    
    def remove_a_node(self, target_node_value):
        """Remove a node from a circular linked list."""

        # when we remove a node, we need to keep in minda
        # that you might be removing the first node,
        # the last node or any node in between. 

        # check if list is empty:
        if self.head is None:
            raise Exception("List is empty!")
        
        current_node = self.head

        # if we remove the head of a circular ll :
        if self.head.data == target_node_value:
            while current_node.next != self.head:
                current_node = current_node.next 
            current_node.next = self.head.next
            self.head = self.head.next 
            return
        
        # if we remove the "tail" of a circular ll
        # or any nodes in between:
        previous = None 
        while current_node.next != self.head:
            previous = current_node
            current_node = current_node.next
            if current_node.data == target_node_value:
                previous.next = current_node.next
                current_node = current_node.next
                return
        
        return "Couldn't find node with that value"