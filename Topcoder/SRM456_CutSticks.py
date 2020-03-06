class CutSticks:
	def maxKth(self, sticks, C, K):
		high = 1000000000
		low = 0
		error = 0.1**9
		prevMid = -1
		while True:
			middle = (high + low) / 2
			midLenStick = 0
			totalCuts = 0
			for i in sticks:
				num = i // middle
				if totalCuts + num-1 > C:
					currentCut = C - totalCuts
				else:
					currentCut = num - 1
				midLenStick += currentCut + 1
				totalCuts += currentCut
			if midLenStick < K:
				high = middle
			elif midLenStick > K:
				low = middle
			else:
				if abs(middle - prevMid) < error:
					return round(middle, 9)
				prevMid = middle
				low = middle


cs = CutSticks()
inpstr = input()
sticks = list(map(int, inpstr.split()))
C = int(input())
K = int(input())
print(cs.maxKth(sticks, C, K))
