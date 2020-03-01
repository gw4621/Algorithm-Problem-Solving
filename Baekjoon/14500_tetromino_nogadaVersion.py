import sys

moyang = (
	( (0, 0), (0, 1), (0, 2), (0, 3) ),
	( (0, 0), (1, 0), (2, 0), (3, 0) ),
	( (0, 0), (0, 1), (1, 0), (1, 1) ),
	( (0, 0), (1, 0), (2, 0), (2, 1) ),
	( (0, 0), (0, 1), (0, 2), (-1, 2) ),
	( (0, 0), (0, 1), (1, 1), (2, 1) ),
	( (0, 0), (1, 0), (0, 1), (0, 2) ),
	( (0, 0), (1, 0), (2, 0), (2, -1) ),
	( (0, 0), (0, 1), (0, 2), (1, 2) ),
	( (0, 0), (0, 1), (1, 0), (2, 0) ),
	( (0, 0), (1, 0), (1, 1), (1, 2) ),
	( (0, 0), (1, 0), (1, 1), (2, 1) ),
	( (0, 0), (1, 0), (0, 1), (1, -1) ),
	( (0, 0), (1, 0), (0, 1), (-1, 1) ),
	( (0, 0), (0, 1), (1, 1), (1, 2) ),
	( (0, 0), (0, 1), (0, 2), (1, 1) ),
	( (0, 0), (1, 0), (1, 1), (2, 0) ),
	( (0, 0), (0, 1), (-1, 1), (0, 2) ),
	( (0, 0), (1, 0), (2, 0), (1, -1) )
)

def getLocalMaxSum(N, M, board, r, c):
	maxTotal = 0
	for i in moyang:
		total = 0
		for j in i:
			total += board[r+j[0]][c+j[1]]
		maxTotal = max(maxTotal, total)
	return maxTotal

def getMaxSum(N, M, board):
	maxSum = 0
	for i in range(1, N+1):
		for j in range(1, M+1):
			maxSum = max(maxSum, getLocalMaxSum(N, M, board, i, j))
	return maxSum


N, M = list(map(int, sys.stdin.readline().split()))
board = [[0 for _ in range(M+4)]]
for _ in range(N):
	board.append([0] + list(map(int, sys.stdin.readline().split())) + [0, 0, 0])
board.append([0 for _ in range(M+4)])
board.append([0 for _ in range(M+4)])
board.append([0 for _ in range(M+4)])

print(getMaxSum(N, M, board))