toAdd = 2
triNum = [1]

def findIdx(a):
	start = 0
	last = len(triNum)
	while True:
		mid = (start + last) // 2
		#print((start, last, mid))
		if mid == 0:
			return 0
		elif triNum[mid] >= a and triNum[mid-1] < a:
			return mid
		if triNum[mid] > a:
			last = mid
		elif triNum[mid] < a:
			start = mid + 1


T = int(input())
for test_case in range(1, T+1):
	a, b = list(map(int, input().split()))
	if a > b:
		a, b = b, a
	elif a == b:
		print(f'#{test_case} 0')
		continue
	while b > triNum[-1]:
		triNum.append(triNum[-1] + toAdd)
		toAdd += 1
	#print(triNum)
	aIdx = findIdx(a)
	bIdx = findIdx(b)
	aDiff = [a-triNum[aIdx-1]-1, triNum[aIdx]-a]
	bDiff = [b-triNum[bIdx-1]-1, triNum[bIdx]-b]
	if aDiff[0] > bDiff[0]:
		print(f'#{test_case} {bIdx-aIdx+abs(aDiff[0]-bDiff[0])}')
	elif aDiff[1] > bDiff[1]:
		print(f'#{test_case} {bIdx-aIdx+abs(bDiff[1]-aDiff[1])}')
	else:
		print(f'#{test_case} {bIdx-aIdx}')