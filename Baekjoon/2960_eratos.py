def findAnswer(N, K):
	erased = [False for _ in range(N+1)]
	smallestNotErased = 2
	totalErase = 0
	while True:
		eraseIdx = smallestNotErased
		while eraseIdx <= N:
			if erased[eraseIdx] == False:
				totalErase += 1
				if totalErase == K:
					return eraseIdx
				erased[eraseIdx] = True
			eraseIdx += smallestNotErased
		for i in range(smallestNotErased+1, N+1):
			if not erased[i]:
				smallestNotErased = i
				break
			
N, K = list(map(int, input().split()))

print(findAnswer(N, K))