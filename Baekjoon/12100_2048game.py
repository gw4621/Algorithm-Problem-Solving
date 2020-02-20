import sys

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def moveBoard(bs, direction):   # board state, direction
	ns = [x[:] for x in bs]
	if direction == RIGHT:
		ns = [[ns[i][N-1-j] for j in range(N)] for i in range(N)]
	elif direction == UP:
		ns = [[ns[i][j] for i in range(N)] for j in range(N)]
	elif direction == DOWN:
		ns = [[ns[i][j] for i in range(N)] for j in range(N)]
		ns = [[ns[i][N-1-j] for j in range(N)] for i in range(N)]
	for i in range(N):
		newList = []
		for j in range(N):
			if ns[i][j] > 0:
				newList.append(ns[i][j])
		idx = 0
		while idx+1 < len(newList):
			if newList[idx] == newList[idx+1]:
				newList[idx] = newList[idx] << 1
				del newList[idx+1]
			idx += 1
		for j in range(len(newList)):
			ns[i][j] = newList[j]
		for j in range(len(newList), N):
			ns[i][j] = 0
	if direction == RIGHT:
		ns = [[ns[i][N-1-j] for j in range(N)] for i in range(N)]
	elif direction == UP:
		ns = [[ns[i][j] for i in range(N)] for j in range(N)]
	elif direction == DOWN:
		ns = [[ns[i][N-1-j] for j in range(N)] for i in range(N)]
		ns = [[ns[i][j] for i in range(N)] for j in range(N)]
	return ns

def get2dMax(bs):
	return max([max(i) for i in bs])

def getAnswer(N, board):
	stack = [(board[:], i, 1, ['UP' if i==0 else 'DOWN' if i==1 else 'LEFT' if i==2 else 'RIGHT']) for i in range(4)]
	maxNum = get2dMax(board)
	#f = open("debug.txt", 'w')
	while len(stack) > 0:
		cmove = stack.pop()	# Current Move
		nextBoard = moveBoard(cmove[0], cmove[1])
		#f.write(str(cmove[2]) + '\n' + str(cmove[3]) + '\n')
		#for i in nextBoard:
		#	for j in i:
		#		f.write(str(j) + ' ')
		#	f.write('\n')
		#f.write('\n')
		maxNum = max(maxNum, get2dMax(nextBoard))
		if cmove[2] < 5:
			for i in range(4):
				dirList = cmove[3][:]
				dirList.append('UP' if i==0 else 'DOWN' if i==1 else 'LEFT' if i==2 else 'RIGHT')
				stack.append(([x[:] for x in nextBoard], i, cmove[2]+1, dirList))
	#f.close()
	return maxNum

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
print(getAnswer(N, board))