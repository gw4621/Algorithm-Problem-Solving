from collections import defaultdict

r, c, k = list(map(int, input().split()))
A = []
for _ in range(3):
	A.append(list(map(int, input().split())))
rowNum = 3
colNum = 3



def rowCal(arr):
	newarr = []
	maxlen = 0
	for row in arr:
		dd = defaultdict(lambda:0)
		for num in row:
			dd[num] += 1
		newrow = sorted(dd.items, key=lambda x:(x[1]<<20)+x[0])
		newarr.append([])
		for i in newrow:
			newarr[-1] += i
		maxlen = max(maxlen, len(newarr[-1]))
	return newarr

def colCal(arr):
	newarr = [[arr[i][j] for i in range(len(arr[0]))] for j in range(len(arr))]
	newarr = rowCal(newarr)


