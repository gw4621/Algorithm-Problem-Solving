import sys
from collections import deque

EMPTY = 0
WALL = 1
ACT_V = 2
INACT_V = -1

N, M = list(map(int, sys.stdin.readline().split()))
vx = []
vy = []
vNum = 0
lab = [[WALL for _ in range(N+2)]]
emptyNum = 0
for i in range(N):
	lab.append([WALL] + list(map(int, sys.stdin.readline().split())) + [WALL])
	for j in range(N):
		if lab[i+1][j+1] == ACT_V:
			vx.append(j+1)
			vy.append(i+1)
			vNum += 1
			lab[i+1][j+1] = INACT_V
		elif lab[i+1][j+1] == EMPTY:
			emptyNum += 1
lab.append([WALL for _ in range(N+2)])

comb = []

def recur_getMinTime(idx):
	if len(comb) == M:
		return virusBfs()
	if idx >= vNum:
		return -1
	comb.append(idx)
	r1 = recur_getMinTime(idx+1)
	comb.pop()
	r2 = recur_getMinTime(idx+1)
	if r1 < 0 and r2 < 0:
		return -1
	elif r1 < 0:
		return r2
	elif r2 < 0:
		return r1
	return min([r1, r2])

posq = deque()
timeq = deque()

def virusBfs():
	posq.clear()
	timeq.clear()
	copyLab = [x[:] for x in lab]
	infectNum = 0
	for i in comb:
		posq.append((vx[i], vy[i]))
		copyLab[vy[i]][vx[i]] = ACT_V
		timeq.append(0)
	if infectNum == emptyNum:
		return 0
	while len(posq) > 0:
		x, y = posq.popleft()
		t = timeq.popleft()
		for i in range(-1, 2, 2):
			if copyLab[y+i][x] <= 0:
				if copyLab[y+i][x] == EMPTY:
					infectNum += 1
				posq.append((x, y+i))
				copyLab[y+i][x] = ACT_V
				timeq.append(t+1)
			if copyLab[y][x+i] <= 0:
				if copyLab[y][x+i] == EMPTY:
					infectNum += 1
				posq.append((x+i, y))
				copyLab[y][x+i] = ACT_V
				timeq.append(t+1)
		if infectNum == emptyNum:
			return t+1
	return -1

print(recur_getMinTime(0))