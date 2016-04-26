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
			else:
				n.walkable = True
			searchSpace.append(n)
			yd.append(y)
			
	Start = searchSpace[0]
	Goal = searchSpace[99]
	
	for a in searchSpace:
		a.setH(Goal)
	
	pygame.init()
	id = (xd,yd)
	
	pygame.display.set_caption("Astar")
	done = False
		
	Traveler = Astar(searchSpace, Start, Goal, id)
	# -----------------------------------------------------
	while not done:
		Traveler.Run()
		pygame.display.flip()
	pygame.quit()
	
main()