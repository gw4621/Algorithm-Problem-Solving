import sys

rowDir = (-1, 0, 1, 0)
colDir = (0, 1, 0, -1)

def simulate(N, M, r, c, d, room):
	cleaned = 0
	while True:
		if room[r][c] == 0:	# 1
			room[r][c] = 2
			cleaned += 1

		dirCount = 0
		while True:	# 2
			d = (d-1)%4
			dirCount += 1
			nextR = r + rowDir[d]
			nextC = c + colDir[d]
			if room[nextR][nextC] == 0:	# 2.a
				r = nextR
				c = nextC
				break
			if dirCount == 4:	# 2.c, 2.d
				backD = (d+2)%4
				nextR = r + rowDir[backD]
				nextC = c + colDir[backD]
				if room[nextR][nextC] == 1:	# 2.d
					return cleaned
				else:	# 2.c
					r = nextR
					c = nextC
					dirCount = 0
	return cleaned

N, M = list(map(int, sys.stdin.readline().split()))
r, c, d = list(map(int, sys.stdin.readline().split()))
room = []
for _ in range(N):
	room.append(list(map(int, sys.stdin.readline().split())))
print(simulate(N, M, r, c, d, room))