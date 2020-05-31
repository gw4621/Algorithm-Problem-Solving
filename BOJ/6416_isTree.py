import sys
from collections import defaultdict

input = sys.stdin.readline

def isTree(link, nonRoot, nodeSet):
	if len(nodeSet) == 0:
		return True
	rootSet = nodeSet - nonRoot
	if len(rootSet) != 1:
		return False
	root = rootSet.pop()
	stack = [root]
	visited = defaultdict(lambda : False)
	while stack:
		cn = stack.pop()
		if visited[cn]:
			return False
		visited[cn] = True
		stack += link[cn]
	while nodeSet:
		if not visited[nodeSet.pop()]:
			return False
	return True

link = defaultdict(lambda : [])
nonRoot = set()
nodeSet = set()

test_case = 0
end = False
while True:
	lineList = list(map(int, input().split()))
	lenth = len(lineList)
	for i in range(lenth//2):
		u, v = lineList[i*2], lineList[i*2+1]
		if u == 0 and v == 0:
			test_case += 1
			if isTree(link, nonRoot, nodeSet):
				print(f'Case {test_case} is a tree.')
			else:
				print(f'Case {test_case} is not a tree.')
			link.clear()
			nonRoot.clear()
			nodeSet.clear()
			continue
		if u < 0 and v < 0:
			end = True
			break
		link[u].append(v)
		nonRoot.add(v)
		nodeSet.add(u)
		nodeSet.add(v)
	if end:
		break
