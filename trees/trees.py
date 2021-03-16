# Terminology:
# node -> basic unit
# children -> nodes directly below a node
# descendants -> nodes below a node
# parent -> node that is directly abovea node
# ancestor -> node that is above a node
# root nod -> node at the top of the three
# left node -> node without any children 
# Examples:
# a filesystem is a tree
# html dom is a tree
# taxonomy is a tree

class Node(object):
    """Node in a tree."""
    
    def __init__(self, data, children):
        self.data = data
        self.children = children 

    def __repr__(self):
        """Reader-friendly representation."""
        
        return f"Node is {self.data}"
    
