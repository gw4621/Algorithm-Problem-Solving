import sys

N = int(sys.stdin.readline())
schedule = [0]

for _ in range(N):
	schedule.append(list(map(int, sys.stdin.readline().split())))

def solve():
	maxProfit = [0 for _ in range(N+1)]
	for i in range(1, N+1):
		nextIdx = i + schedule[i][0] - 1
		if nextIdx <= N:
			profit = maxProfit[i-1] + schedule[i][1]
			maxProfit[nextIdx] = max(maxProfit[nextIdx], profit)
		maxProfit[i] = max(maxProfit[i], maxProfit[i-1])
	return maxProfit[N]
			
print(solve())