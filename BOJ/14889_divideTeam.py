import sys
from itertools import combinations

N = int(sys.stdin.readline())
S = []
for _ in range(N):
	S.append(list(map(int, sys.stdin.readline().split())))
newS = [x[:] for x in S]
for i in range(N):
	for j in range(N):
		newS[i][j] += S[j][i]

totalSet = set(range(N))
combList = combinations(range(N-1), N//2)

minDiff = float('inf')
for i in combList:
	difference = 0
	for j in combinations(i, 2):
		difference += newS[j[0]][j[1]]
	otherTeam = totalSet - set(i)
	for j in combinations(otherTeam, 2):
		difference -= newS[j[0]][j[1]]
	minDiff = min(minDiff, abs(difference))
print(minDiff)