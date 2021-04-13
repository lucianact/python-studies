class SinglyLinkedList(object):
    """A singly linked list."""

    def __init__(self, head=None):
        self.head = None
    

    def prepend_node(self, new_node):
        """Prepend a new node.""" 

        # create a new node:
        new_node = Node(new_node)

        # check if list empty:
        if self.head is None:
            new_node = self.head

        new_node.next = self.head
        self.head = new_node

    
    def append_node(self, new_node):
        """Append a new node."""
        
        # create a new node:
        new_node = Node(new_node)
        
        # check if list is empty:
        if self.head is None:
            self.head = new_node
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        
    
    def print_linked_list(self): 
        """Print linked list."""
        
        # check if list is empty:
        if self.head is None:
            raise Exception("List is empty!")
        
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    
    def find_value(self, node_value):
        """Find specific value in linked list."""
    
        # check if list is empty:
        if self.head is None:
            raise Exception ("List is empty!")
            
        current_node = self.head
        while current_node:
            if current_node.data == node_value:
                return True 
            current_node = current_node.next
            
        return False

    
    def find_length(self):
        """Find out linked list lenght."""
        
        # check if list is empty:
        if self.head is None:
            raise Exception("List is empty!")
        
        current_node = self.head
        lllength = 0  
        while current_node:
            lllength += 1
            current_node = current_node.next
        
        return lllength
    

    def reassign_node_value(self, current_value, new_value):
        """Reassign new value to specific node."""
        
        # check if list is empty:
        if self.head is None:
            raise Exception("List is empty!")
        
        current_node = self.head
        while current_node:
            if current_node.data == current_value:
                current_node.data = new_value
                return current_node.data
            current_node = current_node.next 
        
        return "Value could not be found"
    
  
    def insert_new_node_after(self, target_node, new_node):
        """Insert a new node after specific node."""

        # create new node:
        new_node = Node(new_node)
        
        # check if list is empty:
        if self.head is None:
                raise Exception("Linked list is empty!")
                
        current_node = self.head
        while current_node:
                # 1st. find the target node
                if current_node.data == target_node:
                    # 2nd. twitch a few pointers:
                    # the node which comes aftet the current_node
                    # will now come after the new_node instead: 
                    new_node.next = current_node.next 
                    # then new_node will be the node which
                    # comes after the current node
                    current_node.next = new_node
                current_node = current_node.next 
                

    def insert_new_node_before(self, target_value, new_node):
        """"Insert a new node before specific node."""
        import pdb
        pdb.set_trace()

        # create new node:
        new_node = Node(new_node)
    
        # check if list is empty:
        if self.head is None:
            raise Exception("Linked list is empty!")
        
        # check if head is the target value
        if self.head.data == target_value:
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            if current_node.next.data == target_value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
                # it's necessary to insert a return statement 
                # because after inserting a new node before 
                # a target node/target value, the next node
                # will be once again the same target node/value
            current_node = current_node.next  
    

    def remove_a_node(self, to_be_removed):
        
        # check if we have an empty linked list:
        if self.head is None:
            raise Exception("List is empty!")

        # check if the node to be removed
        # is the head node:
        if self.head.data == to_be_removed:
            self.head = self.head.next 
    
        current_node = self.head 
        while current_node.next:
            if current_node.next.data == to_be_removed:
                current_node.next = current_node.next.next 
            current_node = current_node.next 
            

class Node(object):
    """A node in a linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


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