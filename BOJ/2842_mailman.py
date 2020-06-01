import bisect

dr = (0, 1, 1, -1, 0, -1, 1, -1)
dc = (1, 0, 1, 0, -1, -1, -1, 1)

def dfs(N, level, house, r, c, visited, lo, hi):
	if not (0 <= r < N and 0 <= c < N) or not (lo <= level[r][c] <= hi) or visited[r][c]:
		return 0
	visited[r][c] = True
	ret = 0
	if (r, c) in house:
		ret += 1
	for i in range(8):
		nr, nc = r + dr[i], c + dc[i]
		ret += dfs(N, level, house, nr, nc, visited, lo, hi)
	return ret
	
N = int(input())
house = set()
level = []
for i in range(N):
	line = input()
	for j in range(N):
		if line[j] == 'P':
			pr, pc = (i, j)
		if line[j] == 'K':
			house.add((i, j))
levelSet = set()
for i in range(N):
	level.append(list(map(int, input().split())))
	for j in level[-1]:
		levelSet.add(j)
levelSet = sorted(list(levelSet))
minhi = 1000000
maxlo = 0
for i in house:
	r, c = i
	minhi = min(minhi, level[r][c])
	maxlo = max(maxlo, level[r][c])
minhiIdx = bisect.bisect_left(levelSet, minhi)
maxloIdx = bisect.bisect_left(levelSet, maxlo)
ans = 1000000
j = 0
for i in range(minhiIdx, len(levelSet)):
	while True:
		if j > maxloIdx:
			break
		visited = [[False for _ in range(N)] for _ in range(N)]
		if dfs(N, level, house, pr, pc, visited, levelSet[j], levelSet[i]) == len(house):
			ans = min(ans, levelSet[i] - levelSet[j])
			j += 1
		else:
			break
print(ans)