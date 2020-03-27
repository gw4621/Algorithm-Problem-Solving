def turnLeft(num):
	return ((num << 1) & 0b11111110) ^ (num >> 7)

def turnRight(num):
	return (num >> 1) ^ ((num & 1) << 7)

def findDigit(num, k):	# Clockwise, from 12
	return (num >> (7 - k)) & 1

def moveCogwheel(cogwheel, cogNum, direction, prev):
	thisCog = cogwheel[cogNum]
	if (prev != cogNum-1) and (cogNum > 1):
		leftCog = cogwheel[cogNum-1]
		if findDigit(thisCog, 6) ^ findDigit(leftCog, 2):
			moveCogwheel(cogwheel, cogNum-1, -direction, cogNum)
	if (prev != cogNum+1) and (cogNum < 4):
		rightCog = cogwheel[cogNum+1]
		if findDigit(thisCog, 2) ^ findDigit(rightCog, 6):
			moveCogwheel(cogwheel, cogNum+1, -direction, cogNum)
	cogwheel[cogNum] = turnLeft(cogwheel[cogNum]) if direction<0 else turnRight(cogwheel[cogNum])

def getScore(cogwheel):
	score = 0
	for i in range(1, 5):
		if findDigit(cogwheel[i], 0) > 0:
			score += 2 ** (i-1)
	return score

cogwheel = [0]
for _ in range(4):
	cogwheel.append(int(input(), 2))
K = int(input())
for _ in range(K):
	cogNum, direction = list(map(int, input().split()))
	moveCogwheel(cogwheel, cogNum, direction, 0)
print(getScore(cogwheel))