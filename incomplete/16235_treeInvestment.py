import sys
N, M, K = list(map(int, sys.stdin.readline().split()))
A = []
tree = [[[] for _ in range(N+1)] for _ in range(N+1)]
deadTree = []
nutrient = [[5 for _ in range(N+1)] for _ in range(N+1)]
A.append([])
for _ in range(N):
	A.append([0]+list(map(int, sys.stdin.readline().split())))
for _ in range(M):
	x, y, z = list(map(int, sys.stdin.readline().split()))
	tree[x][y].append(z)
	tree[x][y].sort(reverse=True)

def simSpring():
	for r in range(1, N+1):
		for c in range(1, N+1):
			for i in range(len(tree[r][c])-1, -1, -1):
				if tree[r][c][i] <= nutrient[r][c]:
					nutrient[r][c] -= tree[r][c][i]
					tree[r][c][i] += 1
				else:
					for j in range(0, i+1):
						deadTree.append((r, c, tree[r][c][j]))
					del tree[r][c][:i+1]
					break

def simSummer():
	for i in deadTree:
		nutrient[i[0]][i[1]] += int(i[2] / 2)
	deadTree.clear()

def rep_corner_edge(r, c):
	for t in tree[r][c]:
		if t % 5 == 0:
			for i in range(-1, 2):
				for j in range(-1, 2):
					if r+i >= 1 and r+i <= N and c+j >= 1 and c+j <= N and not (i==0 and j==0):
						tree[r+i][c+j].append(1)
	

def rep_center(r, c):
	for t in tree[r][c]:
		if t % 5 == 0:
			tree[r-1][c-1].append(1)
			tree[r-1][c].append(1)
			tree[r-1][c+1].append(1)
			tree[r][c-1].append(1)
			tree[r][c+1].append(1)
			tree[r+1][c-1].append(1)
			tree[r+1][c].append(1)
			tree[r+1][c+1].append(1)

def simFall():
	rep_corner_edge(1, 1)
	rep_corner_edge(1, N)
	rep_corner_edge(N, 1)
	rep_corner_edge(N, N)
	for i in range(2, N):
		rep_corner_edge(1, i)
		rep_corner_edge(N, i)
		rep_corner_edge(i, 1)
		rep_corner_edge(i, N)
		for j in range(2, N):
			rep_center(i, j)

def simWinter():
	for i in range(1, N+1):
		for j in range(1, N+1):
			nutrient[i][j] += A[i][j]

def simYear():
	simSpring()
	simSummer()
	simFall()
	simWinter()

def countTree():
	total = 0
	for i in tree:
		for j in i:
			total += len(j)
	return total

def solve():
	year = 0
	while year < K:
		simYear()
		year += 1
	print(countTree())

solve()