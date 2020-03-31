import sys

dr = (0, 0, 0, -1, 1)
dc = (0, 1, -1, 0, 0)

class Piece:
	def __init__(self, r, c, d):
		self.r = r
		self.c = c
		self.d = d

def oneTurn(N, K, board, pieces, pieceMap):
	for i in range(len(pieces)):
		p = pieces[i]
		idxOfI = 0
		for j in pieceMap[p.r][p.c]:
			if j == i:
				break
			idxOfI += 1
		cR = p.r
		cC = p.c
		nextR = cR + dr[p.d]
		nextC = cC + dc[p.d]
		if board[nextR][nextC] == 2:
			p.d ^= 0b111 if p.d > 2 else 0b11
			nextR = cR + dr[p.d]
			nextC = cC + dc[p.d]
			if board[nextR][nextC] == 2:
				continue
		if board[nextR][nextC] == 1:
			partialMap = pieceMap[cR][cC][idxOfI:]
			partialMap = partialMap[::-1]
			tmp = 0
			for j in range(idxOfI, len(pieceMap[cR][cC])):
				pieceMap[cR][cC][j] = partialMap[tmp]
				tmp += 1
		for j in pieceMap[cR][cC][idxOfI:]:
			pieces[j].r = nextR
			pieces[j].c = nextC
		pieceMap[nextR][nextC] += pieceMap[cR][cC][idxOfI:]
		pieceMap[cR][cC] = pieceMap[cR][cC][:idxOfI]

		if len(pieceMap[nextR][nextC]) >= 4:
			return True
	return False

def solve(N, K, board, pieces, pieceMap):
	turn = 1
	while turn <= 1000:
		if oneTurn(N, K, board, pieces, pieceMap):
			return turn
		turn += 1
	return -1

N, K = list(map(int, sys.stdin.readline().split()))
board = [[2 for _ in range(N+2)]]
for _ in range(N):
	board.append([2] + list(map(int, sys.stdin.readline().split())) + [2])
board.append([2 for _ in range(N+2)])
pieces = []
pieceMap = [[[] for _ in range(N+2)] for _ in range(N+2)]
for i in range(K):
	r, c, d = list(map(int, sys.stdin.readline().split()))
	pieces.append(Piece(r, c, d))
	pieceMap[r][c].append(i)
print(solve(N, K, board, pieces, pieceMap))