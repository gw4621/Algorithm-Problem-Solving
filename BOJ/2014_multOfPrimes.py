import sys
import heapq
from collections import defaultdict

K, N = list(map(int, sys.stdin.readline().split()))
pq = []
primes = list(map(int, sys.stdin.readline().split()))
visited = defaultdict(lambda :False)
for i in primes:
	heapq.heappush(pq, i)
	visited[i] = True
it = 0
maxNum = primes[-1]
while True:
	it += 1
	c = heapq.heappop(pq)
	if it==N: break
	for i in primes:
		num = c*i
		if len(pq) > N and num > maxNum:
			break
		if not visited[num]:
			heapq.heappush(pq, num)
			visited[num] = True
			maxNum = max(maxNum, num)
print(c)