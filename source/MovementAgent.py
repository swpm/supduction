#### Copyright (c) 2015, swpm, Jeffrey E. Erickson
#### All rights reserved.
#### See the accompanying LICENSE file for terms of use

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
