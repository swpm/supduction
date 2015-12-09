#!/bin/python

import sys
import pygame
import math
import ZoomSurface
from MovementAgent import MovementAgent
from ZoomSurface import ZoomScreen, ZSurface
from cityloader import load_map

def distance(p0, p1):
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

initial_size = (640, 480)

dot_size = 5

cities = []
possession = []
locations = []

def DrawMap(surface, map_data):
	for entry in map_data:
		if entry["possession"] == 2:
			pygame.draw.circle(surface,0xFF0000, entry["loc"], dot_size, dot_size)
		elif entry["possession"]  == 1:
			pygame.draw.circle(surface, 0x0000FF, entry["loc"], dot_size, dot_size)
		else:
			pygame.draw.circle(surface, 0x00FF00, entry["loc"], dot_size, 1)

	color = 0
	for entry in map_data:
		for link_idx in entry["link_idx"]:
			if map_data[link_idx]["idx"] != link_idx:
				print "Bad Index Entry for link generation"
			
			if entry["possession"] == map_data[link_idx]["possession"]:
				if entry["possession"] == 2:
					color = 0xFF0000
				elif entry["possession"] == 1:
					color = 0x0000FF
				else:
					color = 0xFFFFFF
			else:
				color = 0xFFFFFF	
			pygame.draw.line(surface, color, entry["loc"], map_data[link_idx]["loc"])
	
	pygame.display.flip()


def main():
	agents = []
	map_data = load_map()
	zoom = 1
        pygame.init()
        window = pygame.display.set_mode(initial_size)
        ##window = ZoomScreen((640,480))
        disp_surface = pygame.display.get_surface()
        ##surface = ZSurface(disp_surface, initial_size)
        surface = disp_surface
        pygame.display.flip()
	
	DrawMap(surface, map_data)
	pygame.display.flip()
	myfont = pygame.font.SysFont("monospace", 14)
	label = myfont.render("City", 1, (255,255,255))
	source = 0
	dest = 0
	while True:
		for event in pygame.event.get():
			surface.fill((0,0,0))
			DrawMap(surface, map_data)
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.MOUSEMOTION:
				for city in map_data:
					if distance(pygame.mouse.get_pos(), city["loc"]) < dot_size:
						label = myfont.render(str(city["city"]) + str(city["loc"]),1,(255,255,255))
						surface.blit(label, (city["loc"][0], city["loc"][1]-10))
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 4:
					zoom += 1
					print "Zoom In"
				elif event.button == 5:
					zoom -= 1
					print "Zoom Out"
				else:
					print "MouseButtonUP Event " + str(event)
				if(zoom >= 1):
					old_rect = surface.get_rect()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					source = 1
				elif event.button == 3:
					dest = 40
					newAgent = MovementAgent(source, dest)
					newAgent.FindRoute(map_data)
					agents.append(newAgent)
					
				else:
					print event
			else:
				print event
			pygame.display.flip()


if __name__ == "__main__":
        main()

