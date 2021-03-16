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

# A Linked List is a special type of tree:
# all linked list are trees, not all tres are Linked Lists.
# Linked Lists cannot have more than one child.

# There's no way of going back in a tree;
# if we want to check the whole tree, we should start with the root node.
# You can get anywhere from the root.

 
class Node(object):
    """Node in a tree."""
    
    def __init__(self, data, children):
        self.data = data
        self.children = children 
    
    # Depth First Search
    # (stack behavior -> first in, last out)
    def finding_a_node(self, data):
        """Return node object with this data"""
        
        # self is the instance of a node
        # the node where we call .finding_a_node is where we start

        # when there are multiple not unique data,
        # our search stops at the first one.
        
        to_visit = [self]

        # while there are still things to be visited
        while to_visit:
            current = to_visit.pop()
            
            if current.data == data:
                return current
            
            to_visit.extend(current.children)
    
    # what if we want to find the highest-ranking data? 

    # Breadth First Search
    # (queue behavior -> first in, first out)
    def finding_the_highest_ranking_node(self, data):
        """Return the highest-raking node object with this data"""
        
        to_visit = [self]

        # while there are still things to be visited
        while to_visit:
            current = to_visit.pop(0)
            
            if current.data == data:
                return current
            
            to_visit.extend(current.children)
    
    # def __repr__(self):
    #     """Reader-friendly representation."""
    #     return f"Node is {self.data}"

class Tree(object):
    """A tree."""

    def __init__(self, root):
        self.root = root 
    
    def find_in_tree(self, data):
        return self.root.finding_a_node(data)

    # or

    # def find_in_tree(self, data):
    #     return self.root.finding_the_highest_ranking_node(data)
    
    # def __repr__(self):
    #     """Reader-friendly representation."""
    #     return f"Tree node is {self.root}"


# just to practice, 
# let's start by creating a node:
# student = Node("Luciana", [])
# student.children.append("Python")
# student.children.append("JavaScript")
# student.children prints -> Python, JavaScript

# ________________________________________________________________________

# Binary Search Tree
# each node has a left of a right child  
# nodes can only have maximum of 2 childrens
# Constraints:
# we need to have a balanced tree 
class BinarySearchNode():
    """Binary tree node."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def find(self, sought):
        """Return node with this data."""

        current = self

        while current:
            print("checking", current.data)

            # every choice we make reduces # options by half
            # so the runtime of BTS is O(log n) -> base 2

            if current.data == sought:
                return current
            elif sought < current.data:
                current = current.left
            elif sought > current.data:
                current =  current.right  

    # def __repr__(self):
    #     """Reader-friendly representation."""
    #     return f"Binary node {self.data}"

# _________________________________________________________________________

# Advanced Ideas:
# Moving up -> some trees point up
class ReverseNode():
    """Node that points to its parents."""
    def __init__(self, parent):
        self.parent = parent 

# some point both ways:
# cost of more memory -> you double the size of your tree
class BidirectionalNode():
    """Node that is bidirectional."""
    def __init__(self, parent, children):
        self.parent = parent 
        self.children = children 

# you can store this in databases (no SQL databases)





