## Graph Path Manager
# Keeps a list of the current available paths

class GraphPathManager(object):
    
    def __init__(self, finder, world):
        self.finder = finder
        self.world = world
    
