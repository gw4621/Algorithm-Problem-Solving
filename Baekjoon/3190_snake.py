import sys

WALL = -1
EMPTY = 0
APPLE = 10

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def changeDir(currentDir, turn):
	if currentDir == UP:
		if turn == 'L':
			return LEFT
		elif turn == 'D':
			return RIGHT
	elif currentDir == DOWN:
		if turn == 'L':
			return RIGHT
		elif turn == 'D':
			return LEFT
	elif currentDir == LEFT:
		if turn == 'L':
			return DOWN
		elif turn == 'D':
			return UP
	elif currentDir == RIGHT:
		if turn == 'L':
			return UP
		elif turn == 'D':
			return DOWN
	return -1

def snakeMove(snakePos, snakeDir):
	if snakeDir == UP:
		return [snakePos[0]-1, snakePos[1]]
	elif snakeDir == DOWN:
		return [snakePos[0]+1, snakePos[1]]
	elif snakeDir == LEFT:
		return [snakePos[0], snakePos[1]-1]
	elif snakeDir == RIGHT:
		return [snakePos[0], snakePos[1]+1]
	return None

def checkCollision(board, snakeHead, snake):
	if board[snakeHead[0]][snakeHead[1]] == WALL:
		return True
	for i in snake:
		if snakeHead[0] == i[0] and snakeHead[1] == i[1]:
			return True
	return False

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

# Initialize board and snake
board = [[EMPTY for _ in range(N+2)] for _ in range(N+2)]
for i in range(N+2):
	board[i][0] = WALL
	board[0][i] = WALL
	board[i][N+1] = WALL
	board[N+1][i] = WALL
snake = []
snake.append([1, 1])
snakeDir = RIGHT

# Put apple on the board
for _ in range(K):
	applePos = list(map(int, sys.stdin.readline().split()))
	board[applePos[0]][applePos[1]] = APPLE

# Get Direction Change Information
L = int(sys.stdin.readline())
dirChange = []
for i in range(L):
	inpStr = sys.stdin.readline().split()
	dirChange.append([int(inpStr[0]), inpStr[1]])

# Now MOVE
dirChangeIdx = 0
eTime = 0
while True:
	eTime += 1
	newHead = snakeMove(snake[-1], snakeDir)
	if checkCollision(board, newHead, snake):
		break
	snake.append(newHead)

	if board[newHead[0]][newHead[1]] == APPLE:
		board[newHead[0]][newHead[1]] = EMPTY
	else:
		del snake[0]
	if dirChangeIdx < L and eTime == dirChange[dirChangeIdx][0]:
		snakeDir = changeDir(snakeDir, dirChange[dirChangeIdx][1])
		dirChangeIdx += 1

print(eTime)