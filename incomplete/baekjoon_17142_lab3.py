import sys
from collections import deque

EMPTY = 0
WALL = 1
ACT_V = 2
INACT_V = 3

N, M = list(map(int, sys.stdin.readline().split()))
vx = []
vy = []
vNum = 0
lab = [[WALL for _ in range(N+2)]]
for i in range(N):
	lab.append([WALL] + list(map(int, sys.stdin.readline().split())) + [WALL])
	for j in range(N):
		if lab[i+1][j+1] == ACT_V:
			vx.append(j+1)
			vy.append(i+1)
			vNum += 1
			lab[i+1][j+1] = INACT_V
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

def checkComplete(_lab):
	for i in _lab:
		for j in i:
			if j <= 0:
				return False
	return True

posq = deque()
timeq = deque()

def virusBfs():
	posq.clear()
	timeq.clear()
	copyLab = [x[:] for x in lab]
	for i in comb:
		posq.append((vx[i], vy[i]))
		timeq.append(0)
	while len(posq) > 0:
		x, y = posq.popleft()
		t = timeq.popleft()
		copyLab[y][x] = ACT_V
		for i in range(-1, 2, 2):
			if (copyLab[y+i][x] == EMPTY or copyLab[y+i][x] == INACT_V) and (x, y+i) not in posq:
				posq.append((x, y+i))
				timeq.append(t+1)
			if (copyLab[y][x+i] == EMPTY or copyLab[y][x+i] == INACT_V) and (x+i, y) not in posq:
				posq.append((x+i, y))
				timeq.append(t+1)
		if checkComplete(copyLab):
			return t
	return -1

print(recur_getMinTime(0))