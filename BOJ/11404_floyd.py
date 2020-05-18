import sys

input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())
busInfo = [list(map(int, input().split())) for _ in range(m)]
dist = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
	dist[i][i] = 0
for i in busInfo:
	dist[i[0]-1][i[1]-1] = min(dist[i[0]-1][i[1]-1], i[2])
for i in range(n):
	for j in range(n):
		for k in range(n):
			dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
for i in dist:
	for j in i:
		if j == INF:
			print('0', end=' ')
		else:
			print(j, end=' ')
	print()
