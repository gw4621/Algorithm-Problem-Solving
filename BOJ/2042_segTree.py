import sys
import math
from collections import defaultdict

def makeTree(segTree, numList, idx, start, end):
	if start == end:
		segTree[idx] = numList[start]
		return numList[start]
	middle = (start+end)//2
	segTree[idx] = makeTree(segTree, numList, idx*2+1, start, middle) + makeTree(segTree, numList, idx*2+2, middle+1, end)
	return segTree[idx]

def getSum(segTree, idx, start, end, left, right):
	if left <= start and right >= end:
		return segTree[idx]
	if end < left or start > right:
		return 0
	middle = (start+end)//2
	return getSum(segTree, idx*2+1, start, middle, left, right) + getSum(segTree, idx*2+2, middle+1, end, left, right)

def updateTree(segTree, idx, start, end, numIdx, difference):
	if start == end == numIdx:
		segTree[idx] += difference
		return
	if start <= numIdx and end >= numIdx:
		segTree[idx] += difference
		middle = (start+end)//2
		updateTree(segTree, idx*2+1, start, middle, numIdx, difference)
		updateTree(segTree, idx*2+2, middle+1, end, numIdx, difference)
	return

def changeNum(segTree, numList, idx, start, end, numIdx, newNum):
	difference = newNum - numList[numIdx]
	numList[numIdx] = newNum
	updateTree(segTree, 0, 0, N-1, numIdx, difference)
	return

N, M, K = list(map(int, sys.stdin.readline().split()))
numList = []
for _ in range(N):
	numList.append(int(sys.stdin.readline()))
segTree = defaultdict(lambda : 0)
makeTree(segTree, numList, 0, 0, N-1)

for _ in range(M+K):
	a, b, c = list(map(int, sys.stdin.readline().split()))
	if a == 1:
		changeNum(segTree, numList, 0, 0, N-1, b-1, c)
	elif a == 2:
		print(getSum(segTree, 0, 0, N-1, b-1, c-1))