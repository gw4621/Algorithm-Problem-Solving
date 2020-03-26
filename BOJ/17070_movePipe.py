import sys
from collections import defaultdict

N = int(sys.stdin.readline())
room = [[1 for _ in range(N+2)]]
for _ in range(N):
	room.append([1] + list(map(int, sys.stdin.readline().split())) + [1])
room.append([1 for _ in range(N+2)])
ways = defaultdict(lambda :-1)

def solve(N, room, x, y, state):
	global ways
	if(ways[(y, x, state)] >= 0):
		return ways[(y, x, state)]
	answer = 0
	if state == 0:
		if room[y][x] + room[y][x+1] > 0:
			return 0	
		answer += solve(N, room, x+1, y, 0)
		answer += solve(N, room, x+1, y, 2)
	elif state == 1:
		if room[y][x] + room[y+1][x] > 0 :
			return 0
		answer += solve(N, room, x, y+1, 1)
		answer += solve(N, room, x, y+1, 2)
	else:
		if room[y][x] + room[y][x+1] + room[y+1][x] + room[y+1][x+1] > 0:
			return 0
		answer += solve(N, room, x+1, y+1, 0)
		answer += solve(N, room, x+1, y+1, 1)
		answer += solve(N, room, x+1, y+1, 2)
	ways[(y, x, state)] = answer
	return answer

def start(N, room):
	global ways
	if room[N][N] == 1:
		return 0
	if room[N-1][N] == 0:
		ways[(N-1, N, 1)] = 1
	if room[N][N-1] == 0:
		ways[(N, N-1, 0)] = 1
	if room[N-1][N] + room[N][N-1] + room[N-1][N-1] == 0:
		ways[(N-1, N-1, 2)] = 1
	return solve(N, room, 1, 1, 0)

print(start(N, room))