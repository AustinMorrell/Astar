import pygame as gfx
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
		self.color = (0, 0, 255) if (self.walkable) else (255,0,0)
		self.adjacents = []
		self.goal = None

	def draw(self, screen, color):
		margin = self.margin
		color = self.color
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
		
	def setWalk(self, walkable):
		self.walkable = walkable
		 
	def getF(self):
		return self.h + self.g
	def setH(self, Goal):
		self.goal = Goal
		numb = (self.goal.pos[0] - self.pos[0]) + (self.goal.pos[1] - self.pos[1])
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
		
		
	def Run(self):
		#self.Reset()
		open = self.OPEN
		closed = self.CLOSED
		start = self._start
		goal = self._goal
		open.append(start)
		print(open)
		while open:						
			open.sort(key = lambda x : x.f)
			current = open[0]
			open.remove(current)			
			closed.append(current)
			i = 0
			for adj in current.adjacents:
				if adj.walkable and adj not in closed:
					if adj not in open:
						open.append(adj)
						adj.parent = current						
						adj.g = 10 if i < 4 else 14
					else:
						move = 10 if i < 4 else 14
						movecost = move + current.g
						if movecost < adj.g: 
							adj.parent = current						
							adj.g = movecost
							
				i+=1
				
	def GetPath(self, node):
		path = []
		current = node
		while(current != self._start):
			path.append(current.parent)
			current = current.parent
			current.color = (0, 255, 0)
		return path
		
	def SetNeighbors(self):
		Location = 0
		for a in range(99):
			if self.space[a] == self._current:
				Location = a;
		top = self.space[Location - 10]
		bot = self.space[Location + 10]
		left = self.space[Location - 1]
		right = self.space[Location + 1]
		b_left = self.space[Location +9]
		b_right = self.space[Location + 11]
		t_left = self.space[Location - 11]
		t_right = self.space[Location - 9]
		self._current.adjacents = [top, bot, left, right, b_left, b_right, t_left, t_right]