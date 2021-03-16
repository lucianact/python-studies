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
