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
			n.walkable = False if (x >= 5 and x <= 6 and y >= 5 and y <= 8) else True
			searchSpace.append(n)
			yd.append(y)
			
	Start = searchSpace[0]
	Goal = searchSpace[99]
	
	for a in searchSpace:
		a.setH(Goal)
	
	pygame.init()
	id = (xd,yd)
	#WINDOW_SIZE = [255, 255]
	#screen = pygame.display.set_mode(WINDOW_SIZE)
	
	pygame.display.set_caption("Astar")
	done = False
	clock = pygame.time.Clock()
	#screen.fill((0,0,0))
	
	#for i in searchSpace:
		#i.draw(screen, (255, 255, 255))
		
	Traveler = Astar(searchSpace, Start, Goal, id)
	# -----------------------------------------------------
	while not done:
		Traveler.Run()
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
	pygame.quit()
	
main()