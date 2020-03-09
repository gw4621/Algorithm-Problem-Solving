def calculate(num1, num2, oper):
	if oper == 0:
		return num1+num2
	elif oper == 1:
		return num1-num2
	elif oper == 2:
		return num1*num2
	elif oper == 3:
		if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
			return -(-num1 // num2)
		else:
			return num1 // num2
		
def findMinMax(N, A, operList):
	stack = []
	for i in range(len(operList)):
		if operList[i] > 0:
			newOperList = operList[:]
			newOperList[i] -= 1
			stack.append((calculate(A[0], A[1], i), 2, newOperList))
	minVal = float('inf')
	maxVal = float('-inf')
	while len(stack) > 0:
		c = stack.pop()
		if c[1] == N:
			minVal = min(minVal, c[0])
			maxVal = max(maxVal, c[0])
			continue
		for i in range(len(c[2])):
			if c[2][i] > 0:
				newOperList = c[2][:]
				newOperList[i] -= 1
				stack.append((calculate(c[0], A[c[1]], i), c[1]+1, newOperList))
	return minVal, maxVal
N = int(input())
A = list(map(int, input().split()))
operList = list(map(int, input().split()))
minVal, maxVal = findMinMax(N, A, operList)
print(maxVal)
print(minVal)