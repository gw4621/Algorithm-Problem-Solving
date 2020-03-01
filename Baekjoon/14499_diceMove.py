import sys

UP = 3
RIGHT = 1
LEFT = 2
DOWN = 4
posMove = [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]

def moveUp(dice):
	newDice = [dice[i] for i in range(6)]
	newDice[0] = dice[3]
	newDice[1] = dice[0]
	newDice[2] = dice[1]
	newDice[3] = dice[2]
	return newDice
def moveDown(dice):
	newDice = [dice[i] for i in range(6)]
	newDice[0] = dice[1]
	newDice[1] = dice[2]
	newDice[2] = dice[3]
	newDice[3] = dice[0]
	return newDice
def moveLeft(dice):
	newDice = [dice[i] for i in range(6)]
	newDice[2] = dice[4]
	newDice[4] = dice[0]
	newDice[5] = dice[2]
	newDice[0] = dice[5]
	return newDice
def moveRight(dice):
	newDice = [dice[i] for i in range(6)]
	newDice[5] = dice[0]
	newDice[0] = dice[4]
	newDice[4] = dice[2]
	newDice[2] = dice[5]
	return newDice

def diceMove(N, M, x, y, dice, board, direction):
	newy = y + posMove[direction][0]
	newx = x + posMove[direction][1]
	if not ((0 <= newx < N) and (0 <= newy < M)):
		return x, y, dice, board
	
	if direction==UP:
		dice = moveUp(dice)
	elif direction==DOWN:
		dice = moveDown(dice)
	elif direction==LEFT:
		dice = moveLeft(dice)
	else:
		dice = moveRight(dice)
	if board[newx][newy] > 0:
		dice[2] = board[newx][newy]
		board[newx][newy] = 0
	else:
		board[newx][newy] = dice[2]
	print(dice[0])
	return newx, newy, dice, board


def solve(N, M, x, y, K, board, order):
	dice = [0, 0, 0, 0, 0, 0]
	diceX = x
	diceY = y
	for i in order:
		diceX, diceY, dice, board = diceMove(N, M, diceX, diceY, dice, board, i)

N, M, x, y, K = list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(N):
	board.append(list(map(int, sys.stdin.readline().split())))
order = list(map(int, sys.stdin.readline().split()))

solve(N, M, x, y, K, board, order)