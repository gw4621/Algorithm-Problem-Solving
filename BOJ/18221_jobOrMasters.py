import sys
import math

room = []
N = int(sys.stdin.readline())
for i in range(N):
	room.append(list(map(int, sys.stdin.readline().split())))
	for j in range(N):
		if room[i][j] == 2:
			sgPos = (i, j)
		elif room[i][j] == 5:
			profPos = (i, j)


def sum2d(l, xPos, yPos):
	total = 0
	for i in range(yPos[0], yPos[1]+1):
		for j in range(xPos[0], xPos[1]+1):
			total += l[i][j]
	return total


def canEscape(sgPos, profPos):
	xPos = sorted([sgPos[1], profPos[1]])
	yPos = sorted([sgPos[0], profPos[0]])
	if math.sqrt(pow(sgPos[0]-profPos[0], 2)+pow(sgPos[1]-profPos[1], 2)) < 5:
		return False
	if sum2d(room, xPos, yPos) >= 3+2+5:
		return True

if canEscape(sgPos, profPos):
	print(1)
else:
	print(0)