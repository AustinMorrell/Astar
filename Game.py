import pygame
from Astar import *

def main():
	searchSpace = []
	for x in range(10):
		for y in range(10):
			n = Node(x, y)
			n.walkable = True
			searchSpace.append(n)

	pygame.init()
	
	WINDOW_SIZE = [255, 255]
	screen = pygame.display.set_mode(WINDOW_SIZE)
	
	pygame.display.set_caption("Astar")
	done = False
	clock = pygame.time.Clock()
	screen.fill((0,0,0))
	
	for i in searchSpace:
		i.draw(screen, (255, 255, 255))
		
	Start = searchSpace[0]
	Goal = searchSpace[99]
	Traveler = Astar(searchSpace, Start, Goal)
	
	# -----------------------------------------------------
	while not done:
		
		clock.tick(60)
		pygame.display.flip()
	pygame.quit()
	
main()