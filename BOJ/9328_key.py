import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

T = int(input())

dq = deque()

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

for test_case in range(1, T+1):
	touchedDoor = set()
	newlyAccessable = []
	h, w = map(int, input().split())
	board = []
	doors = defaultdict(lambda : [])
	for r in range(h):
		board.append(list(input().strip()))
		for c in range(w):
			if ord('A') <= ord(board[r][c]) <= ord('Z'):
				doors[board[r][c]].append((r, c))
	keyString = input().strip()
	if keyString == '0':
		keyString = ''
	for ch in keyString:
		for r, c in doors[ch.upper()]:
			board[r][c] = '.'

	visited = [[False for _ in range(w)] for _ in range(h)]
	keys = set()
	answer = 0

	for i in range(h):
		if not visited[i][0]:
			if board[i][0] == '.':
				dq.append((i, 0))
				visited[i][0] = True
			elif board[i][0] == '$':
				answer += 1
				board[i][0] = '.'
				dq.append((i, 0))
				visited[i][0] = True
			elif ord('A') <= ord(board[i][0]) <= ord('Z'):
				touchedDoor.add((board[i][0], i, 0))
				visited[i][0] = True
			elif ord('a') <= ord(board[i][0]) <= ord('z'):
				keys.add(board[i][0])
				board[i][0] = '.'
				visited[i][0] = True
		if not visited[i][w-1]:
			if board[i][w-1] == '.':
				dq.append((i, w-1))
				visited[i][w-1] = True
			elif board[i][w-1] == '$':
				answer += 1
				board[i][w-1] = '.'
				dq.append((i, w-1))
				visited[i][w-1] = True
			elif ord('A') <= ord(board[i][w-1]) <= ord('Z'):
				touchedDoor.add((board[i][w-1], i, w-1))
				visited[i][w-1] = True
			elif ord('a') <= ord(board[i][w-1]) <= ord('z'):
				keys.add(board[i][w-1])
				board[i][w-1] = '.'
				visited[i][w-1] = True
	for j in range(w):
		if not visited[0][j]:
			if board[0][j] == '.':
				dq.append((0, j))
				visited[0][j] = True
			elif board[0][j] == '$':
				answer += 1
				board[0][j] = '.'
				dq.append((0, j))
				visited[0][j] = True
			elif ord('A') <= ord(board[0][j]) <= ord('Z'):
				touchedDoor.add((board[0][j], 0, j))
				visited[0][j] = True
			elif ord('a') <= ord(board[0][j]) <= ord('z'):
				keys.add(board[0][j])
				board[0][j] = '.'
				visited[0][j] = True
		if not visited[h-1][j]:
			if board[h-1][j] == '.':
				dq.append((h-1, j))
				visited[h-1][j] = True
			elif board[h-1][j] == '$':
				answer += 1
				board[h-1][j] = '.'
				dq.append((h-1, j))
				visited[h-1][j] = True
			elif ord('A') <= ord(board[h-1][j]) <= ord('Z'):
				touchedDoor.add((board[h-1][j], h-1, j))
				visited[h-1][j] = True
			elif ord('a') <= ord(board[h-1][j]) <= ord('z'):
				keys.add(board[h-1][j])
				board[h-1][j] = '.'
				visited[h-1][j] = True
	
	while dq:	# First BFS
		r, c = dq.popleft()
		for d in range(4):
			nr, nc = r+dr[d], c+dc[d]
			if 0<=nr<h and 0<=nc<w and not visited[nr][nc]:
				if board[nr][nc] == '.':
					dq.append((nr, nc))
					visited[nr][nc] = True
				elif board[nr][nc] == '$':
					answer += 1
					board[nr][nc] = '.'
					dq.append((nr, nc))
					visited[nr][nc] = True
				elif ord('A') <= ord(board[nr][nc]) <= ord('Z'):
					touchedDoor.add((board[nr][nc], nr, nc))
					visited[nr][nc] = True
				elif ord('a') <= ord(board[nr][nc]) <= ord('z'):
					keys.add(board[nr][nc])
					board[nr][nc] = '.'
					visited[nr][nc] = True
					dq.append((nr, nc))
	# First BFS end
	# First newlyAccessable
	toRemove = []
	for door in touchedDoor:
		if door[0].lower() in keys:
			board[door[1]][door[2]] = '.'
			newlyAccessable.append((door[1], door[2]))
			toRemove.append(door)
	while toRemove:
		touchedDoor.remove(toRemove.pop())

	# Until there is no newly accessable, do bfs
	while newlyAccessable:
		while newlyAccessable:
			dq.append(newlyAccessable.pop())

		while dq:	# BFS
			r, c = dq.popleft()
			for d in range(4):
				nr, nc = r+dr[d], c+dc[d]
				if 0<=nr<h and 0<=nc<w and not visited[nr][nc]:
					if board[nr][nc] == '.':
						dq.append((nr, nc))
						visited[nr][nc] = True
					elif board[nr][nc] == '$':
						answer += 1
						board[nr][nc] = '.'
						dq.append((nr, nc))
						visited[nr][nc] = True
					elif ord('A') <= ord(board[nr][nc]) <= ord('Z'):
						touchedDoor.add((board[nr][nc], nr, nc))
						visited[nr][nc] = True
					elif ord('a') <= ord(board[nr][nc]) <= ord('z'):
						keys.add(board[nr][nc])
						board[nr][nc] = '.'
						visited[nr][nc] = True
						dq.append((nr, nc))

		for door in touchedDoor:
			if door[0].lower() in keys:
				board[door[1]][door[2]] = '.'
				newlyAccessable.append((door[1], door[2]))
				toRemove.append(door)
		while toRemove:
			touchedDoor.remove(toRemove.pop())
	print(answer)