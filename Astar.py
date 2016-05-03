import pygame as gfx
WINDOW_SIZE = [255, 255]
screen = gfx.display.set_mode(WINDOW_SIZE)
screen.fill((0,0,0))
clock = gfx.time.Clock()

class Node:
	def __init__(self, x, y):
		self.parent = None		
		self.color = None
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) *  x + self.margin
		self.top = (self.margin + self.height) *  y + self.margin
		self.walkable = None
		self.pos = (x, self.height - y)
		self.f = None
		self.g = None
		self.h = None
		self.adjacents = []
		self.goal = None

	def draw(self, screen):
		margin = self.margin
		color = self.color
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
		gfx.time.wait(5)
		gfx.display.flip()	
		
	def setColor(self):
		if self.walkable == True: 
			self.color = (0, 0, 255)  
		else:
			self.color = (255,0,0)
	
	def setF(self):
		self.f = self.h + self.g
	
	def setH(self, Goal):
		self.goal = Goal
		numb = abs(self.goal.pos[0] - self.pos[0]) + abs(self.pos[1] - self.goal.pos[1])
		self.h = numb
		
class Astar:
	def __init__(self, SearchSpace, Start, Goal, dims):
		self.OPEN = []
		self.CLOSED = []
		self.space = SearchSpace
		self._start = Start
		self._goal = Goal
		self._current = self._start
		self.rows = dims[0]
		self.cols = dims[1]
		
		
	def GetPath(self, node):
		path = []
		self._current = node
		while(self._current != self._start):
			path.append(self._current.parent)
			self._current = self._current.parent
			self._current.color = (0, 255, 0)
			print(self._current.parent)
		return path
		
	def SetNeighbors(self):
		Location = 0
		for a in range(99):
			if self.space[a] == self._current:
				Location = a;
		if Location - 10 < 100 and Location - 10 > -1:
			self.space[Location - 10].g = 10
			self._current.adjacents.append(self.space[Location - 10])
		if Location + 10 < 100 and Location + 10 > -1:
			self.space[Location + 10].g = 10
			self._current.adjacents.append(self.space[Location + 10])
		if Location - 1 < 100 and Location - 1 > -1:
			self.space[Location - 1].g = 10
			self._current.adjacents.append(self.space[Location - 1])
		if Location + 1 < 100 and Location + 1 > -1:
			self.space[Location + 1].g = 10
			self._current.adjacents.append(self.space[Location + 1])
		if Location + 9 < 100 and Location + 9 > -1:
			self.space[Location + 9].g = 14
			self._current.adjacents.append(self.space[Location + 9])
		if Location + 11 < 100 and Location + 11 > -1:
			self.space[Location + 11].g = 14
			self._current.adjacents.append(self.space[Location + 11])
		if Location - 11 < 100 and Location - 11 > -1:
			self.space[Location - 11].g = 14
			self._current.adjacents.append(self.space[Location - 11])
		if Location - 9 < 100 and Location - 9 > -1:
			self.space[Location - 9].g = 14
			self._current.adjacents.append(self.space[Location - 9])
		
	def drawPath(self, screen, color):
		path = self.GetPath(self._goal)
		for a in path:
			margin = a.margin
			color = a.color
			gfx.draw.rect(screen, color, (a.left , a.top, a.width, a.height))
		gfx.display.flip()
		
	def Run(self):
		self.OPEN.append(self._current)
		
		while True:
		
			self.OPEN.remove(self._current)
			self._current.color = (117,117,117)
			self.CLOSED.append(self._current)
			
			for i in self.space:
				i.draw(screen)			
			
			self.SetNeighbors()
			for i in self._current.adjacents:
				if i not in self.CLOSED and i.walkable == True:
					i.setF()
					i.parent = self._current
					i.color = (255,145,0)
					self.OPEN.append(i)
				else:
					print("No can do, buddy!")
			self.OPEN.sort(key = lambda x : x.f)
			self._current = self.OPEN[0]
			self.OPEN.append(self._current)
			if self._current == self._goal or len(self.OPEN) <= 0:
				break
				
		self.drawPath(screen, (0, 255, 0))
			