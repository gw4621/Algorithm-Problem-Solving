import sys

input = sys.stdin.readline

board = []

blank = []
candidate = []


def getCandidate(r, c):
	cand = set((1, 2, 3, 4, 5, 6, 7, 8, 9))
	baseR = (r // 3) * 3
	baseC = (c // 3) * 3
	for i in range(9):
		if board[r][i] in cand:
			cand.remove(board[r][i])
		if board[i][c] in cand:
			cand.remove(board[i][c])
	for i in range(3):
		for j in range(3):
			if board[baseR+i][baseC+j]  in cand:
				cand.remove(board[baseR+i][baseC+j])
	return cand

for _ in range(9):
	board.append( list(map(int, input().split() ) ) )

for i in range(9):
	for j in range(9):
		if board[i][j] == 0:
			blank.append((i, j))

isAnswer = False

def solve(idx):
	global isAnswer
	if idx == len(blank):
		isAnswer = True
		return
	r, c = blank[idx]
	cand = getCandidate(r, c)

	while cand:
		board[r][c] = cand.pop()
		solve(idx+1)
		if isAnswer:
			return
		board[r][c] = 0
		
if blank:
	solve(0)

str_list = []
for i in range(9):
	for j in range(9):
		str_list.append(str(board[i][j]))
		str_list.append(' ')
	str_list.append('\n')
print(''.join(str_list))