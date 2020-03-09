from collections import defaultdict

r, c, k = list(map(int, input().split()))
r -= 1
c -= 1
A = []
for _ in range(3):
	A.append(list(map(int, input().split())))

def rowCal(arr):
	newarr = []
	maxlen = 0
	for row in arr:
		dd = defaultdict(lambda:0)
		for num in row:
			if num > 0:
				dd[num] += 1
		newrow = sorted(dd.items(), key=lambda x:(x[1]<<20)+x[0])
		newarr.append([])
		for i in newrow:
			newarr[-1] += i
		maxlen = max(maxlen, len(newarr[-1]))
	maxlen = min(100, maxlen)
	for i in range(len(newarr)):
		if len(newarr[i]) > maxlen:
			newarr[i] = newarr[i][0:maxlen]
		else:
			newarr[i] += [0 for _ in range(maxlen - len(newarr[i]))]
	return newarr

def colCal(arr):
	newarr = [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]
	newarr = rowCal(newarr)
	return [[newarr[i][j] for i in range(len(newarr))] for j in range(len(newarr[0]))]

def solve(A):
	currentTime = 0
	if len(A) > r and len(A[0]) > c:
		if A[r][c] == k:
			return 0
	while currentTime < 100:
		currentTime += 1
		if len(A) < len(A[0]):
			A = colCal(A)
		else:
			A = rowCal(A)
		if len(A) > r and len(A[0]) > c:
			if A[r][c] == k:
				return currentTime
	return -1

print(solve(A))
