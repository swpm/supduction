## The graph edge class

## This class describes a link between cities.
## Attributes:
###     lCity: the "left" city (one end of the link)
###     rCity: the "right" city (the other end of the link)

## Eventually, this link object will have more uses, like tracking distance and occupancy

class GraphLink(object):
    
    def __init__(self, lCity, rCity):
        self.lCity = lCity
        self.rCity = rCity
        
    def LinksSame(self, compLink):
        if compLink.lCity == self.lCity:
            if compLink.rCity == self.rCity:
                return True
        
        if compLink.lCity == self.rCity:
            if compLink.rCity == self.lCity:
                return True
        return False
        