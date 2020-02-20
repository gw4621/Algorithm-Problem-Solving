from collections import deque

def solve(N):
	if N == 1:
		return 0
	elif N <= 3:
		return 1
	numList = [i for i in range(N+1)]
	Q = deque([(2, 1), (3, 1)])
	while len(Q) > 0:
		st = Q.popleft()
		if st[0] <= N and numList[st[0]] > st[1]:
			numList[st[0]] = st[1]
			Q.append((st[0]+1, st[1]+1))
			Q.append((st[0]*2, st[1]+1))
			Q.append((st[0]*3, st[1]+1))
	return numList[N]

N = int(input())
print(solve(N))