import pygame as gfx
WINDOW_SIZE = [255, 255]
screen = gfx.display.set_mode(WINDOW_SIZE)
screen.fill((0,0,0))

class Node:
	def __init__(self, x, y):
		self.parent = None		
		self.color = (255,255,255)
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) *  x + self.margin
		self.top = (self.margin + self.height) *  y + self.margin
		self.walkable = True
		self.pos = (x, self.height - y)
		self.f = None
		self.g = None
		self.h = None
		self.color = (0, 0, 255) if (self.walkable == True) else (255,0,0)
		self.adjacents = []
		self.goal = None

	def draw(self, screen, color):
		margin = self.margin
		color = self.color
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
		gfx.display.flip()
		
	def setWalk(self, walkable):
		self.walkable = walkable
		 
	def getF(self):
		return self.h + self.g
	def setH(self, Goal):
		self.goal = Goal
		numb = abs(self.goal.pos[0] - self.pos[0]) + abs(self.goal.pos[1] - self.pos[1])
		self.h = numb
	def setG(self, val):
		self.g = val
	def setColor(self, val):
		self.color = val

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
	
	def current(self):
		return self._current
		
	def current(self, value):
		self._current = value
		
	#def draw(self, screen, color):
		
		
	def GetPath(self, node):
		path = []
		current = node
		while(current != self._start):
			path.append(current.parent)
			current = current.parent
			current.color = (0, 255, 0)
		print(path)
		return path
		
	def SetNeighbors(self):
		Location = 0
		for a in range(99):
			if self.space[a] == self._current:
				Location = a;
		if Location - 10 < 100 and Location - 10 > -1:
			top = self.space[Location - 10]
			top.g = 10
			self._current.adjacents.append(top)
		if Location + 10 < 100 and Location + 10 > -1:
			bot = self.space[Location + 10]
			bot.g = 10
			self._current.adjacents.append(bot)
		if Location - 1 < 100 and Location - 1 > -1:
			left = self.space[Location - 1]
			left.g = 10
			self._current.adjacents.append(left)
		if Location + 1 < 100 and Location + 1 > -1:
			right = self.space[Location + 1]
			right.g = 10
			self._current.adjacents.append(right)
		if Location + 9 < 100 and Location + 9 > -1:
			b_left = self.space[Location + 9]
			b_left.g = 14
			self._current.adjacents.append(b_left)
		if Location + 11 < 100 and Location + 11 > -1:
			b_right = self.space[Location + 11]
			b_right.g = 14
			self._current.adjacents.append(b_right)
		if Location - 11 < 100 and Location - 11 > -1:
			t_left = self.space[Location - 11]
			t_left.g = 14
			self._current.adjacents.append(t_left)
		if Location - 9 < 100 and Location - 9 > -1:
			t_right = self.space[Location - 9]
			t_right.g = 14
			self._current.adjacents.append(t_right)
		
	def FindLowestF(self):
		lowestF = self._current.adjacents[0].f
		theNode = self._current.adjacents[0]
		for a in self._current.adjacents:
			a.f = a.getF
			if a.f < lowestF:
				lowestF = a.f
				theNode = a
		return theNode
		
	def Run(self):
		#self.Reset()
		while self._current.parent != self._goal:
			for i in self.space:
				i.draw(screen, (255, 255, 255))
			self.OPEN.append(self._current)
			self.SetNeighbors()
			for a in self._current.adjacents:
				a.parent = self._current
				self.OPEN.append(a)
			self.OPEN.remove(self._current)
			self.CLOSED.append(self._current)
			self._current = self.FindLowestF()
			for event in gfx.event.get():
				if event.type == gfx.QUIT: sys.exit()
			
		self.GetPath(self._goal)
			