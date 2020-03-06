import sys

class MazeMaker:
	def longestPath(self, maze, startRow, startCol, moveRow, moveCol):
		height = len(maze)
		width = len(maze[0])
		dist = [[-1 for _ in range(width)] for _ in range(height)]
		numMaze = height * width
		for i in range(height):
			for j in range(width):
				if maze[i][j] == 'X' or maze[i][j] == 'x':
					dist[i][j] = -2
					numMaze -= 1
		revisit = [[False]*width]*height
		numVisited = 0
		numRevisit = 0
		queue = [(startRow, startCol, 0)]
		time = 0
		while True:
			pos = queue.pop(0)
			time = pos[2]
			if dist[pos[0]][pos[1]] < 0:
				dist[pos[0]][pos[1]] = time
				numVisited += 1
				for i in range(len(moveRow)):
					movedPos = (pos[0]+moveRow[i], pos[1]+moveCol[i])
					if movedPos[0]>=0 and movedPos[0]<height and movedPos[1]>=0 and movedPos[1]<width and maze[movedPos[0]][movedPos[1]]=='.':
						queue.append((movedPos[0], movedPos[1], time+1))
			else:
				if not revisit[pos[0]][pos[1]]:
					revisit[pos[0]][pos[1]] = True
					numRevisit += 1
			if numVisited <= numRevisit or numVisited == numMaze or (not queue):
				break

		toret = 0
		for i in dist:
			for j in i:
				if j == -1:
					toret = -1
					break
				elif j > toret:
					toret = j
			if toret == -1:
				break

		return toret

maze = []
while True:
	inpstr = input()
	if inpstr.isdigit():
		startRow = int(inpstr)
		break
	else:
		maze.append(inpstr)
startCol = int(input())
moveRow = list(map(int, input().split(', ')))
moveCol = list(map(int, input().split(', ')))

mm = MazeMaker()
print(mm.longestPath(maze, startRow, startCol, moveRow, moveCol))
