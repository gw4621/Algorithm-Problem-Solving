import sys

def check(N, A, x, y, d1, d2):
	area = [0 for _ in range(5)]
	done = [[False for _ in range(N+1)] for _ in range(N+1)]
	r = x
	startc = y
	endc = y
	while True:
		for c in range(startc, endc+1):
			area[4] += A[r][c]
			done[r][c] = True
		if r < x+d1:
			startc -= 1
		else:
			startc += 1
		if r < x+d2:
			endc += 1
		else:
			endc -= 1
		r += 1
		if startc == endc:
			area[4] += A[r][startc]
			done[r][startc] = True
			break		
	for r in range(1, N+1):
		for c in range(1, N+1):
			if done[r][c]:
				continue
			if r < x+d1 and c <= y:
				area[0] += A[r][c]
			elif r <= x+d2 and y < c:
				area[1] += A[r][c]
			elif x+d1 <= r and c < y-d1+d2:
				area[2] += A[r][c]
			elif x+d2 < r and y-d1+d2 <= c:
				area[3] += A[r][c]
	return max(area) - min(area)


def solve(N, A):
	ans = float('inf')
	for x in range(1, N-2+1):
		for y in range(2, N-1+1):
			for d1 in range(1, min(y-1, N-x-1)+1):
				for d2 in range(1, min(N-x-d1, N-y)+1):
					ans = min(ans, check(N, A, x, y, d1, d2))
	return ans

N = int(sys.stdin.readline())
A = [[0 for _ in range(N+1)]]
for _ in range(N):
	A.append([0]+list(map(int, sys.stdin.readline().split())))
print(solve(N, A))