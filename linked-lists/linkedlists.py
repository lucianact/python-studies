class Node(object):
    """Node in a Linked List."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node data: {self.data}, next node: {self.next.data}" if self.next else None

class NoTailLinkedList(object):
    """Linked List using head only."""
    
    def __init__(self):
        self.head = None
    
    def append_node(self, data):
        """Append node with data to end of list."""

        # creating a node inside the method 
        new_node = Node(data)

        # should the new node be the head of our ll?
        if self.head is None:
            self.head = new_node
        # the last node of the ll will always point to none
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    def print_list(self):
        """Print all items in the list."""

        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next 


class LinkedList(object):
    """Linked List using head and tail."""
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        """Append node with data to the end of the list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        
        if self.tail is not None:
            self.tail.next = new_node
        
        # while the ll is empty:
        self.tail = new_node
    
    def print_list(self):
        """Print all items in the list."""

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def find(self, data):
        """Does this data exist in our list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def remove(self, value):
        """Remove node with given value"""

        # If removing head, make 2nd item (if any) the new .head
        if self.head is not None and self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        # Removing something other than head
        current = self.head

        while current.next is not None:

            if current.next.data == value:
                current.next = current.next.next
                if current.next is None:
                    # If removing last item, update .tail
                    self.tail = current
                return

            else:     # haven't found yet, keep traversing
                current = current.next


