import sys
from itertools import product

def spin(N, M, D, order):
	x, d, k = order
	idx = x
	erase = [[False for _ in range(M)] for _ in range(N+1)]
	hasErase = False
	while idx <= N:	# Spin Disks
		D[idx] = D[idx][-k:] + D[idx][:-k] if d == 0 else D[idx][k:] + D[idx][:k]
		idx += x
	for i in range(1, N):
		for j in range(M-1):
			if D[i][j] == 0:
				continue
			if D[i][j] == D[i][j+1]:
				erase[i][j] = True
				erase[i][j+1] = True
				hasErase = True
			if D[i][j] == D[i+1][j]:
				erase[i][j] = True
				erase[i+1][j] = True
				hasErase = True
		if D[i][M-1] == 0:
			continue
		if D[i][M-1] == D[i][0]:
			erase[i][M-1] = True
			erase[i][0] = True
			hasErase = True
		if D[i][M-1] == D[i+1][M-1]:
			erase[i][M-1] = True
			erase[i+1][M-1] = True
			hasErase = True
	for j in range(M-1):
		if D[N][j] == 0:
			continue
		if D[N][j] == D[N][j+1]:
			erase[N][j] = True
			erase[N][j+1] = True
			hasErase = True
	if D[N][M-1] > 0 and D[N][M-1] == D[N][0]:
		erase[N][M-1] = True
		erase[N][0] = True
		hasErase = True
	
	it = tuple(product(range(1, N+1), range(M)))
	if hasErase:
		for i, j in it:
			if erase[i][j]:
				D[i][j] = 0
		return

	total = [0, 0]
	for i, j in it:
		if D[i][j] > 0:
			total[0] += D[i][j]
			total[1] += 1
	if total[1] == 0:
		return
	mean = total[0] / total[1]
	for i, j in it:
		if D[i][j] > 0:
			if D[i][j] < mean:
				D[i][j] += 1
			elif D[i][j] > mean:
				D[i][j] -= 1
	
def solve(N, M, T, D, orders):
	for i in range(T):
		spin(N, M, D, orders[i])
	return sum(map(sum, D))

N, M, T = list(map(int, sys.stdin.readline().split()))
D = [[]]
for _ in range(N):
	D.append(list(map(int, sys.stdin.readline().split())))
orders = []
for _ in range(T):
	orders.append(list(map(int, sys.stdin.readline().split())))
print(solve(N, M, T, D, orders))