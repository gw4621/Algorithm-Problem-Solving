import sys
input = sys.stdin.readline

N = int(input())
prerequisite = [[] for _ in range(N)]
isPreOf = [[] for _ in range(N)]
preCount = [0 for _ in range(N)]
buildTime = [0 for _ in range(N)]
totalTime = [0 for _ in range(N)]
buildAble = []
for i in range(N):
	line = list(map(int, input().split()))
	buildTime[i] = line[0]
	preCount[i] = len(line) - 2
	if preCount[i] == 0:
		buildAble.append(i)
	else:
		for j in range(1, len(line)-1):
			prerequisite[i].append(line[j]-1)
			isPreOf[line[j]-1].append(i)
while buildAble:
	m = buildAble.pop()
	preTime = 0
	for i in prerequisite[m]:
		preTime = max(preTime, totalTime[i])
	totalTime[m] = preTime + buildTime[m]
	for i in isPreOf[m]:
		preCount[i] -= 1
		if preCount[i] == 0:
			buildAble.append(i)
for i in totalTime:
	print(i)
