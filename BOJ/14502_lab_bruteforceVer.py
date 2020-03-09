import sys
from itertools import combinations

EMPTY = 0
WALL = 1
VIRUS = 2

direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def spreadVirusCountSafe(lab, virusList, emptyCount):
	stack = [i for i in virusList]
	while len(stack) > 0:
		cVirus = stack.pop()
		if not (lab[cVirus[0]][cVirus[1]] == VIRUS):
			lab[cVirus[0]][cVirus[1]] = VIRUS
			emptyCount -= 1
			for d in direction:
				nextRow = cVirus[0] + d[0]
				nextCol = cVirus[1] + d[1]
				nextSpace = (nextRow, nextCol)
				if lab[nextRow][nextCol] == EMPTY:
					stack.append(nextSpace)
	return emptyCount
	

def solve(N, M, lab, emptyList, virusList):
	emptyCount = len(emptyList) - 3 + len(virusList)
	maxSafe = 0
	for i in combinations(emptyList, 3):
		newLab = [x[:] for x in lab]
		for j in i:
			newLab[j[0]][j[1]] = WALL
		maxSafe = max(maxSafe, spreadVirusCountSafe(newLab, virusList, emptyCount))
	return maxSafe


N, M = list(map(int, sys.stdin.readline().split()))
lab = [[1 for _ in range(M+2)]]
emptyCount = 0
virusList = []
emptyList = []
for i in range(1, N+1):
	lab.append([1] + list(map(int, sys.stdin.readline().split())) + [1])
	for j in range(1, M+1):
		if lab[i][j] == EMPTY:
			emptyList.append((i, j))
		elif lab[i][j] == VIRUS:
			virusList.append((i, j))
			lab[i][j] = EMPTY
lab.append([1 for _ in range(M+2)])

print(solve(N, M, lab, emptyList, virusList))