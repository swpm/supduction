import pygame

class MovementAgent:
	
	def __init__(self, source, dest, id = 0):
		self.position = (0,0)
		self.speed = 5 #pixels per second
		self.destination = dest
		self.id = id
		self.waypoints = []
		self.location = source

	def Update(self, tick):
		return self		

	def FindRoute(self, map_data):
		#starting at location, explore all routes
		#first one to reach destination wins
		explorer =  RecursiveExploration(map_data, self.location, self.destination)
		self.waypoints = explorer.Start()
#		print self.waypoints

class RecursiveExploration:
	def __init__(self, map_data, source, dest):
		self.waypoints = []
		self.source = source
		self.destination = dest
		self.map_data = map_data
		self.ExploreVisited = []
		self.TreeVisited = []
		self.paths = []		
		self.distances = {}

	def Start(self):
		self.MakeTree()
#		print self.distances
#		print "Finding Path..."
		self.FindPath(self.destination)
		return self.waypoints

	def FindPath(self, location):
		if location == self.source:
			self.waypoints.append(location)
			return
		else:
			for node in self.paths:
				if location in node["to"]:
#					print "From: " + str(node["from"]) + " To: " + str(location)
					self.FindPath(node["from"])
					self.waypoints.append(location)
				else:
					continue

	def MakeTree(self):
		self.distances[0] = []
		self.distances[0].append(self.source)
		
		i = 0
#		print "Searching Map, Total Cities = " + str(len(self.map_data))
		while(len(self.TreeVisited) < len(self.map_data)):
			if i == 15:
				break
			newList = []	
			for city in self.distances[i]:
				self.TreeVisited.append(city)

			for city in self.distances[i]:
				newDict = {}
				newDict["from"] = city
				newDict["to"] = []
				for link in self.map_data[city]["link_idx"]:
					if link not in self.TreeVisited:
						if link not in newList:
							newList.append(link)
							newDict["to"].append(link)
				self.paths.append(newDict)
			self.distances[i+1] = newList
#			print "Distance " + str(i+1) + " cities: " + str(self.distances[i+1])
			i = i + 1
#		print str(len(self.TreeVisited)) + " Cities visited with max distance " + str(i)
#		print self.paths
