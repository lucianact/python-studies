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
    def finding_the_highest_ranking_node_(self, data):
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
    
# just to practice, 
# let's start by creating a node:
# student = Node("Luciana", [])
# student.children.append("Python")
# student.children.append("JavaScript")
# student.children prints -> Python, JavaScript




