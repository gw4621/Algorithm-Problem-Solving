import sys

N = int(sys.stdin.readline())
isDragon = [[False for _ in range(101)] for _ in range(101)]

def makeDragon(x, y, d, g):
	generation = 0
	dragonList = [(x, y)]
	if d == 0:
		dragonList.append((x+1, y))
	elif d == 1:
		dragonList.append((x, y-1))
	elif d == 2:
		dragonList.append((x-1, y))
	else:
		dragonList.append((x, y+1))
	pivotIndex = 1
	while generation < g:
		pivP = dragonList[pivotIndex]
		for i in range(pivotIndex-1, -1, -1):
			oldP = dragonList[i]
			newP = (pivP[1] - oldP[1] + pivP[0], oldP[0] - pivP[0] + pivP[1])
			dragonList.append(newP)
		pivotIndex = len(dragonList) - 1
		generation += 1
	for i in dragonList:
		isDragon[i[0]][i[1]] = True

for _ in range(N):
	x, y, d, g = list(map(int, sys.stdin.readline().split()))
	makeDragon(x, y, d, g)

def checkSquare():
	totalDragonSquare = 0
	for i in range(100):
		for j in range(100):
			if isDragon[i][j] and isDragon[i][j+1] and isDragon[i+1][j] and isDragon[i+1][j+1]:
				totalDragonSquare += 1
	return totalDragonSquare

print(checkSquare())