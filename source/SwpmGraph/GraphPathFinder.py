## Graph Path Finder
# Graph to find paths within a Graph World
# May end up being a base class for different finding methods

class GraphPathFinder(object):
    
    def __init__(self, world):
        self.world = world