import sys
N, M, K = list(map(int, sys.stdin.readline().split()))
A = []
tree = [[[] for _ in range(N+1)] for _ in range(N+1)]
deadTree = []
nutrient = [[5 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N):
	A.append(list(map(int, sys.stdin.readline().split())))
for _ in range(M):
	x, y, z = list(map(int, sys.stdin.readline().split()))
	tree[x][y].append(z)
	tree[x][y].sort(reverse=True)

def simSpring():
	for r in range(1, N+1):
		for c in range(1, N+1):
			for i in range(len(tree[r][c])-1, -1, -1):
				if tree[r][c][i]+1 < nutrient[r][c]:
					tree[r][c][i] += 1
					nutrient[r][c] -= tree[r][c][i]
				else:
					for j in range(0, i+1):
						deadTree.append((r, c, tree[r][c][j]+1))
					del tree[r][c][:i+1]
					break

def simSummer():
	for i in deadTree:
		nutrient[i[0]][i[1]] += int(i[2] / 2)
	deadTree.clear()

def corner_edge():

def simFall():
	

def simWinter():


def simYear():


def solve():
	while 