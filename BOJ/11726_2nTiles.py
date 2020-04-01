def solve(n):
	ans = [0, 1, 2, 3, 5, 8]
	while len(ans) < n+1:
		ans.append(ans[-1]+ans[-2])
	return ans[n] % 10007
n = int(input())
print(solve(n))