class Queue(object):
    """A simple queue, implemented using a list."""

    def __init__(self):
        self._data = []

    def enqueue(self, item):
        """Add to end of queue."""
        self._data.append(item)

    def dequeue(self):
        """Remove from front of queue."""
        return self._data.pop(0)

    def peek(self):
        """Show first item in queue."""
        return self._data[0]

    def is_empty(self):
        """Is queue empty?"""
        return not self._data

# Graphs:
# are like tree, excep they contain loops (cycles)
# relantionships can be direct or undirect 
# are often used to model relationship between things
# graphs can be connected or disconnected 
# trees are directed, acyclic graphs
# all trees are graphs, but not all graphs are trees
# trees have a hierarchy, graphs do not 

# Terminology:
# nodes or vertex -> basic unit
# edge or arc -> connecst two nodes
# adjacent -> two nodes are "adjacent" if they share an edge
# adjacency list -> for a given node, a list of every node directly connect to
# weight (optional) -> each edge can have a weight (price, distance, etc)

# Example:
# Airline route map
# -> each node is an airport
# -> each edge is a flight
# -> the weight of each edge is the price
# what's the cheapest way to go from atlanta to oakland? 

# Carpooling
# -> each node is a rider
# -> edges represents possible carpooling matches
# -> only two people can carpool together at a time
# -> how can we match the maximum number os pairs of riders?

# represeing a graph with OOP:
class PersonNode():
    """Node in a graph, representing a person."""

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent."""

        # you can't have the same adjacent node more than once
        # it makes no sense 
        if adjacent is None:
            adjacent = set()
        
        assert isinstance(adjacent, set), \
            "adjacent must be a set!"
        
        self.name = name
        self.adjacent = adjacent
    
    # def __repr__(self):
    #     """Debugging-friendly representation."""
    #     return f'Person node {self.name}'

class FriendGraph():
    """Graph holding people and their friendships."""

    def __init__(self):
        """Create an empty graph."""
        self.nodes = set()

    def add_person(self, person):
        """Add a person to our graph."""
        self.nodes.add(person)
    
    def set_friends(self, person1, person2):
        """Set two people as friends."""
        person1.adjacent.add(person2)
        person2.adjacent.add(person1)
    
    def are_connected(self, person1, person2):
        """Are two people connected?"""
        
        # Breath-first search. why?

        possible_nodes = Queue()
        seen = set()
        possible_nodes.enqueue(person1)
        seen.add(person1) 

        while not possible_nodes.is_empty():
            person = possible_nodes.dequeue()
            print("checking", person)
            if person is person2:
                return True 
            else:
                


# step 1:
# create instances of the node class:
harry = PersonNode("Harry")
hermione = PersonNode("Hermione")
# step 2:
# create a instance of the graph class:
friends = FriendGraph()
# step 3:
# add nodes to the graph
friends.add_person([harry, hermione])
#step 4:
# create relationshop between nodes
friends.set_friends(harry, hermione)

# Let's talking about checking if two nodes are adjancents
# one way of doing this is throught Breath First Search algo
# in case of a graph, BFS will first check all the immediate connections 
# and then gradually go to the next "levels"

