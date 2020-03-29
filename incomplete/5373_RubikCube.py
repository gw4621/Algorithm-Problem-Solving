import sys

class Cube:
	def __init__(self):
		self.cube = [
			[['w','w','w'] for _ in range(3)],
			[['r','r','r'] for _ in range(3)],
			[['b','b','b'] for _ in range(3)],
			[['o','o','o'] for _ in range(3)],
			[['g','g','g'] for _ in range(3)],
			[['y','y','y'] for _ in range(3)]
		]
	def clear(self):
		self.cube[0] = [['w','w','w'] for _ in range(3)]
		self.cube[1] = [['r','r','r'] for _ in range(3)]
		self.cube[2] = [['b','b','b'] for _ in range(3)]
		self.cube[3] = [['o','o','o'] for _ in range(3)]
		self.cube[4] = [['g','g','g'] for _ in range(3)]
		self.cube[5] = [['y','y','y'] for _ in range(3)]
	def moveUpperCw(self):	# Move Upper Layer Clock-wise
		newCube0 = [[self.cube[0][2-j][i] for j in range(3)] for i in range(3)]
		self.cube[0] = newCube0
		tmp = self.cube[1][0]
		self.cube[1][0] = self.cube[2][0]
		self.cube[2][0] = self.cube[3][0]
		self.cube[3][0] = self.cube[4][0]
		self.cube[4][0] = tmp
	def moveUpperCC(self):	# Move Upper Layer Counter Clock-wise
		newCube0 = [[self.cube[0][j][2-i] for j in range(3)] for i in range(3)]
		self.cube[0] = newCube0
		tmp = self.cube[1][0]
		self.cube[1][0] = self.cube[4][0]
		self.cube[4][0] = self.cube[3][0]
		self.cube[3][0] = self.cube[2][0]
		self.cube[2][0] = tmp
	def moveDownCw(self):
		newCube5 = [[self.cube[5][2-j][i] for j in range(3)] for i in range(3)]
		self.cube[5] = newCube5
		tmp = self.cube[1][2]
		self.cube[1][2] = self.cube[4][2]
		self.cube[4][2] = self.cube[3][2]
		self.cube[3][2] = self.cube[2][2]
		self.cube[2][2] = tmp
	def moveDownCC(self):
		newCube5 = [[self.cube[5][j][2-i] for j in range(3)] for i in range(3)]
		self.cube[5] = newCube5
		tmp = self.cube[1][2]
		self.cube[1][2] = self.cube[2][2]
		self.cube[2][2] = self.cube[3][2]
		self.cube[3][2] = self.cube[4][2]
		self.cube[4][2] = tmp
	def moveFrontCw(self):
		newCube1 = [[self.cube[1][2-j][i] for j in range(3)] for i in range(3)]
		self.cube[1] = newCube1
		tmp = self.cube[0][2][:]
		self.cube[0][2] = [self.cube[4][2-i][2] for i in range(3)]
		for i in range(3):
			self.cube[4][i][2] = self.cube[5][0][i]
		self.cube[5][0] = [self.cube[2][2-i][0] for i in range(3)]
		for i in range(3):
			self.cube[2][i][0] = tmp[i]
	def moveFrontCC(self):
		newCube1 = [[self.cube[1][j][2-i] for j in range(3)] for i in range(3)]
		self.cube[1] = newCube1
		tmp = self.cube[0][2][:]
		self.cube[0][2] = [self.cube[2][i][0] for i in range(3)]
		for i in range(3):
			self.cube[2][i][0] = self.cube[5][0][2-i]
		self.cube[5][0] = [self.cube[4][i][2] for i in range(3)]
		for i in range(3):
			self.cube[4][i][2] = tmp[2-i]
	def turnRight(self):
		newCube0 = [[self.cube[0][2-j][i] for j in range(3)] for i in range(3)]
		newCube5 = [[self.cube[5][j][2-i] for j in range(3)] for i in range(3)]
		self.cube[0] = newCube0
		self.cube[5] = newCube5
		tmp = self.cube[1]
		self.cube[1] = self.cube[2]
		self.cube[2] = self.cube[3]
		self.cube[3] = self.cube[4]
		self.cube[4] = tmp
	def turnLeft(self):
		newCube0 = [[self.cube[0][j][2-i] for j in range(3)] for i in range(3)]
		newCube5 = [[self.cube[5][2-j][i] for j in range(3)] for i in range(3)]
		self.cube[0] = newCube0
		self.cube[5] = newCube5
		tmp = self.cube[1]
		self.cube[1] = self.cube[4]
		self.cube[4] = self.cube[3]
		self.cube[3] = self.cube[2]
		self.cube[2] = tmp
	def moveCube(self, direction):
		if direction[0] == 'U':
			if direction[1] == '+':
				self.moveUpperCw()
			else:
				self.moveUpperCC()
		elif direction[0] == 'D':
			if direction[1] == '+':
				self.moveDownCw()
			else:
				self.moveDownCC()
		else:
			if direction[0] == 'R':
				self.turnRight()
			elif direction[0] == 'B':
				self.turnRight()
				self.turnRight()
			elif direction[0] == 'L':
				self.turnLeft()
			if direction[1] == '+':
				self.moveFrontCw()
			else:
				self.moveFrontCC()
			if direction[0] == 'R':
				self.turnLeft()
			elif direction[0] == 'B':
				self.turnRight()
				self.turnRight()
			elif direction[0] == 'L':
				self.turnRight()
	def showUp(self):
		for i in range(3):
			for j in range(3):
				print(self.cube[0][i][j], end='')
			print()

c = Cube()
T = int(sys.stdin.readline())
for _ in range(T):
	n = int(sys.stdin.readline())
	order = sys.stdin.readline().split()
	for d in order:
		c.moveCube(d)
	c.showUp()
	c.clear()
