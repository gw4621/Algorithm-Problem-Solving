from collections import deque
import sys

N, M = list(map(int, sys.stdin.readline().split()))
board = []
for i in range(N):
	board.append(list(sys.stdin.readline().strip()))
	for j in range(M):
		if board[i][j] == 'B':
			bPos = [i, j]
			board[i][j] = '.'
		elif board[i][j] == 'R':
			rPos = [i, j]
			board[i][j] = '.'
		elif board[i][j] == 'O':
			hole = [i, j]
board.append(['#', '.', '.', '#'])
board.append(['#', '#', '#', '#'])
def solve():
	moveQueue = deque()
	moveQueue.append(((0, -1), bPos, rPos, 1))
	moveQueue.append(((0, +1), bPos, rPos, 1))
	moveQueue.append(((-1, 0), bPos, rPos, 1))
	moveQueue.append(((+1, 0), bPos, rPos, 1))

	while len(moveQueue) > 0:
		cmove, cbPos, crPos, ctime = moveQueue.popleft()	# Current Move, Current Blue Position, so on
		bStop = False
		rStop = False
		fail = False
		success = False
		while not (bStop and rStop):
			nbPos = [cbPos[0] + cmove[0], cbPos[1] + cmove[1]]	# Next Blue Position
			nrPos = [crPos[0] + cmove[0], crPos[1] + cmove[1]]	# Next Red Position
			nbBoard = board[nbPos[0]][nbPos[1]]	# Estimated Next Blue Board
			nrBoard = board[nrPos[0]][nrPos[1]] # Estimated Next Red Board
			if nbBoard == '#':
				nbPos = cbPos
				bStop = True
			if nrBoard == '#':
				nrPos = crPos
				rStop = True
			if nbPos == nrPos:
				if rStop and bStop:
					print('BUG')
				elif bStop:
					nrPos = crPos
					rStop = True
				elif rStop:
					nbPos = cbPos
					bStop = True
				else:
					print('BUG2')
			nbBoard = board[nbPos[0]][nbPos[1]]	# Real Next Blue Board
			nrBoard = board[nrPos[0]][nrPos[1]]	# Real Next Blue Board
			if nbBoard == 'O':
				fail = True
				nbPos = [N, 1] if nrPos == [N, 2] else [N, 2]
				crPos = nrPos
				cbPos = nbPos
				break
			if nrBoard == 'O':
				success = True
				nrPos = [N, 2] if nbPos == [N, 1] else [N, 1]
			crPos = nrPos
			cbPos = nbPos
		if fail: continue
		if success: return ctime
		if ctime > 9: continue
		# Move Complete, set next move
		if cmove[0] == 0:
			moveQueue.append(((+1, 0), cbPos, crPos, ctime+1))
			moveQueue.append(((-1, 0), cbPos, crPos, ctime+1))
		else:
			moveQueue.append(((0, +1), cbPos, crPos, ctime+1))
			moveQueue.append(((0, -1), cbPos, crPos, ctime+1))
	return -1
print(solve())