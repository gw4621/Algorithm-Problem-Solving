from collections import deque

MAXPAR = 18

def makeTreeInfo(N, pInput):
	parent = [[1 for _ in range(MAXPAR)] for _ in range(N+1)]
	child = [[] for _ in range(N+1)]
	depth = [1 for _ in range(N+1)]
	for i in range(len(pInput)):
		parent[i+2][0] = pInput[i]
		child[pInput[i]].append(i+2)
		depth[i+2] = depth[pInput[i]] + 1
	st = []
	for i in child[1]:
		st.append(i)
	while len(st) > 0:
		c = st.pop()
		for i in range(1, MAXPAR):
			parent[c][i] = parent[parent[c][i-1]][i-1]
		for i in child[c]:
			st.append(i)
	return parent, child, depth

def howManyLink(parent, depth, a, b):	# Use LCA method
	ancA = a
	ancB = b
	# Make same depth
	if depth[a] > depth[b]:
		ancA = parent[a][0]
	elif depth[a] < depth[b]:
		ancB = parent[b][0]
	lca = ancA
	if ancA != ancB:
		for i in range(MAXPAR-1, -1, -1):
			if parent[ancA][i] != parent[ancB][i]:
				ancA = parent[ancA][i]
				ancB = parent[ancB][i]
			lca = parent[ancA][i]
	#print(f'{a}, {b}, {lca}')	# Debug: see nodes and lca
	return depth[a] + depth[b] - depth[lca] - depth[lca]
	
def solve(N, pInput):
	parent, child, depth = makeTreeInfo(N, pInput)
	dq = deque()
	for i in child[1]:
		dq.appendleft(i)
	answer = 0
	prev = 1
	while len(dq) > 0:
		c = dq.pop()
		answer += howManyLink(parent, depth, c, prev)
		for i in child[c]:
			dq.appendleft(i)
		prev = c
	return answer

T = int(input())
for i in range(T):
	N = int(input())
	pInput = list(map(int, input().split()))
	makeTreeInfo(N, pInput)
	print('#{} {}'.format(i+1, solve(N, pInput)))