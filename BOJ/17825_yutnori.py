score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 40, 0]
# Total 32 places (except goal, 0~31), Exceptions: 5->20, 10->23, 15->25 when stopped, 22->28, 24->28, 19->31 whenever

def dfs(value, turn, pos, cs):
	if turn == 10:
		return cs
	cVal = value[turn]
	ans = 0
	for i in range(4):
		if pos[i] < 0:
			continue
		newPos = pos[:]
		if newPos[i] == 5:
			newPos[i] = 20
		elif newPos[i] == 10:
			newPos[i] = 23
		elif newPos[i] == 15:
			newPos[i] = 25
		elif newPos[i] == 22 or newPos[i] == 24:
			newPos[i] = 28
		elif newPos[i] == 19:
			newPos[i] = 31
		else:
			newPos[i] += 1
		tmp = 1
		while tmp < cVal:
			if newPos[i] == 22 or newPos[i] == 24:
				newPos[i] = 28
			elif newPos[i] == 19:
				newPos[i] = 31
			else:
				newPos[i] += 1			
			tmp += 1
		if newPos[i] > 31:
			newPos[i] = -1
		unavailable = False
		for j in range(4):
			if newPos[i] == -1:
				break
			if i != j and newPos[i] == newPos[j]:
				unavailable = True
		if unavailable:
			continue
		ans = max(ans, dfs(value, turn+1, newPos, cs + score[newPos[i]]))
	return ans
	
def solve(value):
	return dfs(value, 0, [0, 0, 0, 0], 0)

value = list(map(int, input().split()))
print(solve(value))