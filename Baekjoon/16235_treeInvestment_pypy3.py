import sys
from collections import deque

N, M, K = list(map(int, sys.stdin.readline().split()))
A = []
tree = [[deque() for _ in range(N+2)] for _ in range(N+2)]
nutrient = [[5 for _ in range(N+2)] for _ in range(N+2)]
deadTreeNutrient = [[0 for _ in range(N+2)] for _ in range(N+2)]
A.append([])
for _ in range(N):
	A.append([0]+list(map(int, sys.stdin.readline().split())))
for _ in range(M):
	x, y, z = list(map(int, sys.stdin.readline().split()))
	tree[x][y].append(z)

willReproduce = []

def simSpring():
	willReproduce.clear()
	for r in range(1, N+1):
		for c in range(1, N+1):
			surviveTree = deque()
			while len(tree[r][c]) > 0:
				thisTree = tree[r][c].pop()
				if thisTree <= nutrient[r][c]:
					nutrient[r][c] -= thisTree
					surviveTree.appendleft(thisTree + 1)
					if (thisTree + 1) % 5 == 0:
						willReproduce.append((r, c))
				else:
					deadTreeNutrient[r][c] += int(thisTree / 2)
					while len(tree[r][c]) > 0:
						thisTree = tree[r][c].pop()
						deadTreeNutrient[r][c] += int(thisTree / 2)
					break
			tree[r][c] = surviveTree

def reproduce(r, c):
	tree[r-1][c-1].append(1)
	tree[r-1][c].append(1)
	tree[r-1][c+1].append(1)
	tree[r][c-1].append(1)
	tree[r][c+1].append(1)
	tree[r+1][c-1].append(1)
	tree[r+1][c].append(1)
	tree[r+1][c+1].append(1)


def simFall():
	for i in willReproduce:
		reproduce(i[0], i[1])

def simWinter():
	for i in range(1, N+1):
		for j in range(1, N+1):
			nutrient[i][j] += A[i][j] + deadTreeNutrient[i][j]
			deadTreeNutrient[i][j] = 0

def simYear():
	simSpring()
	simFall()
	simWinter()

def countTree():
	total = 0
	for i in range(1, N+1):
		for j in range(1, N+1):
			total += len(tree[i][j])
	return total

def solve():
	year = 0
	while year < K:
		simYear()
		year += 1
	print(countTree())

solve()