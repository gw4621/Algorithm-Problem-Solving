import sys
import itertools
from collections import defaultdict
def find(group, pos):
	r, c = pos
	if group[r][c] == (r, c):
		return (r, c)
	group[r][c] = find(group, group[r][c])
	return group[r][c]
def union(group, pos1, pos2, total):
	parent1 = find(group, pos1)
	parent2 = find(group, pos2)
	if parent1 == parent2:
		return
	r1, c1 = parent1
	r2, c2 = parent2
	group[r2][c2] = parent1
	total[r1][c1][0] += total[r2][c2][0]
	total[r1][c1][1] += total[r2][c2][1]
	total[r2][c2][0] = 0
	total[r2][c2][1] = 0
def solve(N, L, R, P, group, total):
	turn = 0
	itpro = tuple(itertools.product(range(N), repeat=2))
	average = defaultdict(lambda: 0)
	while True:
		hasChanged = False
		for i, j in itpro:
			total[i][j][0] = P[i][j]
			total[i][j][1] = 1
			group[i][j] = (i, j)
		for i, j in itpro:
			if j+1 < N:
				if L <= abs(P[i][j] - P[i][j+1]) <= R:
					union(group, (i, j), (i, j+1), total)
					hasChanged = True 
			if i+1 < N:
				if L <= abs(P[i][j] - P[i+1][j]) <= R:
					union(group, (i, j), (i+1, j), total)
					hasChanged = True
		if not hasChanged:
			return turn
		turn += 1
		average.clear()
		for i, j in itpro:
			if total[i][j][0] > 0:
				average[(i, j)] = total[i][j][0] // total[i][j][1]
		for i, j in itpro:
			parent = find(group, (i, j))
			P[i][j] = average[parent]

N, L, R = list(map(int, sys.stdin.readline().split()))
P = []
for _ in range(N):
	P.append(list(map(int, sys.stdin.readline().split())))
total = [[[P[i][j], 1] for j in range(N)] for i in range(N)]
group = [[(i, j) for j in range(N)] for i in range(N)]
print(solve(N, L, R, P, group, total))