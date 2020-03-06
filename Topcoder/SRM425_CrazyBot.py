import sys

class CrazyBot:
	def dfs(self, currentN, visited, posX, posY):
		if (posX, posY) in visited:
			return 0
		elif currentN == self.n:
			return 1
		else:
			visited.add((posX, posY))
			return self.east*self.dfs(currentN+1, visited, posX+1, posY) + self.west*self.dfs(currentN+1, visited, posX-1, posY) + self.south*self.dfs(currentN+1, visited, posX, posY-1) + self.north*self.dfs(currentN+1, visited, posX, posY+1)
	def getProbability(self, n, east, west, south, north):
		self.n = n
		self.east = east/100
		self.west = west/100
		self.south = south/100
		self.north = north/100
		visited = set([])
		return self.dfs(0, visited, 0, 0)

n = int(sys.stdin.readline())
east = int(sys.stdin.readline())
west = int(sys.stdin.readline())
south = int(sys.stdin.readline())
north = int(sys.stdin.readline())


cb = CrazyBot()
print(cb.getProbability(n, east, west, south, north))
