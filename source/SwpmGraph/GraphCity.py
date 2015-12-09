##  City Class

## This is the class that represents a city
###     idx: the index or numerical id of the city
###     name: the city's name, a string
###     location: a 2-tuple of x, y coordinates
###     links: a list of GraphLink objects that link this GraphCity to others
###     facilities: a list of Facilities in the city
###     possession: who controls the city


class GraphCity():
    
    def __init__(self, idx, name, x_loc, y_loc, possession):
        self.idx = idx
        self.name = name
        self.location = (x_loc, y_loc)
        self.links = []
        self.facilities = []
        self.possession = possession
        
    def AddLink(self, newLink):
        for link in self.links:
            if link.LinksSame(newLink):
                return
        self.links.append(newLink)
        
    def toString(self):
        string = str(self.name) + " " + str(self.location) + " Links: "
        for link in self.links:
            string = string + str((link.lCity, link.rCity)) + " "
        string = string + str(self.possession)
        return string
