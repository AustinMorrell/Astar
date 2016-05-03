import os
import sys
import pygame
from Astar import *

def main():
	xd = []
	yd = []
	searchSpace = []
	for x in range(10):
		xd.append(x)
		for y in range(10):
			n = Node(x, y)
			if x >= 5 and x <= 6 and y >= 5 and y <= 8:
				n.walkable = False
			elif x == 0 or y == 0 or x == 9 or y == 9:
				n.walkable = False
			else:
				n.walkable = True
			n.setColor()
			searchSpace.append(n)
			yd.append(y)
			
	s = input("Enter a Start: ")
	g = input("Enter a Goal: ")
	Start = searchSpace[s]
	Goal = searchSpace[g]
	Goal.color = (255,255,0)
	
	for a in searchSpace:
		a.setH(Goal)
	
	pygame.init()
	id = (xd,yd)
	
	pygame.display.set_caption("Astar")
	done = False
		
	Traveler = Astar(searchSpace, Start, Goal, id)
	# -----------------------------------------------------
	Traveler.Run()
	d = raw_input("Press Enter to continue...")
	os.system('cls')
	main()
	pygame.quit()
	
main()