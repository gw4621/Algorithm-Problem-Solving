import sys

def solve(n, k, value):
	inf = float('inf')
	ans = [inf for _ in range(k+1)]
	ans[0] = 0
	for i in range(n):
		for j in range(k+1):
			if ans[j] == inf:
				continue
			nextVal = j+value[i]
			if nextVal <= k:
				ans[nextVal] = min(ans[nextVal], ans[j]+1)
	return ans[k] if ans[k] != inf else -1

n, k = list(map(int, sys.stdin.readline().split()))
value = []
for _ in range(n):
	value.append(int(sys.stdin.readline()))
print(solve(n, k, value))