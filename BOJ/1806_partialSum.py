import sys
N, S = list(map(int, sys.stdin.readline().split()))
numList = list(map(int, sys.stdin.readline().split()))
start = 0
end = 1
total = numList[0]
answer = float('inf')
while True:
	if total < S:
		if end < N:
			end += 1
			total += numList[end-1]
		else:
			break
	elif total >= S:
		answer = min(answer, end-start)
		total -= numList[start]
		start += 1
		if start == end:
			if end < N:
				end += 1
				total += numList[end-1]
			else:
				break
if answer==float('inf'):
	print(0)
else:
	print(answer)