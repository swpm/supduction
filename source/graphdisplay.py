#!/usr/bin/python

#### Copyright (c) 2015, swpm, Jeffrey E. Erickson
#### All rights reserved.
#### See the accompanying LICENSE file for terms of use

import sys
from SwpmGraph import GraphWorldLoader

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def main():
	loader = GraphWorldLoader()
	world =	loader.load_map()
	map_data = world.cities
	
	x = []
	y = []
	lines = []
	for city in map_data:
		x.append(city.location[0])
		y.append(city.location[1])
		for link in city.links:
			if link.lCity == city.idx:
				for otherCity in map_data:
					if otherCity.idx == link.rCity:
						line_x = []
						line_y = []
						line_x.append(city.location[0])
						line_x.append(otherCity.location[0])
						line_y.append(city.location[1])
						line_y.append(otherCity.location[1])
						line = Line2D(line_x, line_y)
						lines.append(line)
			else:
				for otherCity in map_data:
					if otherCity.idx == link.lCity:
						line_x = []
						line_y = []
						line_x.append(city.location[0])
						line_x.append(otherCity.location[0])
						line_y.append(city.location[1])
						line_y.append(otherCity.location[1])
						line = Line2D(line_x, line_y)
						lines.append(line)
					
	fig = plt.figure()
	ax = fig.add_subplot(111)
	for line in lines:
		ax.add_line(line)
	plt.scatter(x, y)
	plt.show()
	


if __name__ == "__main__":
        main()

