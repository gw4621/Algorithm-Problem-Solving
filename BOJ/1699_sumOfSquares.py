import math

def solve(N):
	ans = [i for i in range(N+1)]
	found = [False for _ in range(N+1)]
	biggestSquare = int(math.sqrt(N))
	squares = [i*i for i in range(biggestSquare+1)]
	for i in range(1, biggestSquare+1):
		idx = squares[i]
		ans[idx] = 1
		found[idx] = True

	def dfs(num, ans, found, squares):
		if found[num]:
			return ans[num]
		sq = int(math.sqrt(num))
		for i in range(sq, 1, -1):
			ans[num] = min(ans[num], dfs(num-squares[i], ans, found, squares)+1)
		found[num] = True
		return ans[num]
		
	return dfs(N, ans, found, squares)

N = int(input())
print(solve(N))