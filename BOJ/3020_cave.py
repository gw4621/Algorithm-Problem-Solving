import sys
import bisect

input = sys.stdin.readline

N, H = map(int, input().split())
top = []
down = []
for obs in range(N//2):
	down.append(int(input()))
	top.append(int(input()))
top.sort()
down.sort()
minObs = float('inf')
for i in range(1, H+1):
	obsCount = len(down) - bisect.bisect_left(down, i)
	obsCount += len(top) - bisect.bisect_left(top, H-i+1)
	if obsCount < minObs:
		minObs = obsCount
		sameObs = 1
	elif obsCount == minObs:
		sameObs += 1
print(f'{minObs} {sameObs}')