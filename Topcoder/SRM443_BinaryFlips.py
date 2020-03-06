class BinaryFlips:
	def minimalMoves(self, A, B, K):	# Make A become 0. Make A become multiple of K
		if A == 0:
			return 0

		total = A + B
		toFlip = A
		
		if total < K or (total == K and toFlip != K) or (toFlip % 2 == 1 and K % 2 == 0):
			return -1

		moves = 0

		multOfK = (toFlip % K == 0)
		while not multOfK:
			ableMove = [i for i in range((-1)*min(K, 2*toFlip-K), min(K, 2*(total-toFlip)-K)+1, 2)]
			for i in ableMove:
				if (toFlip + i) % K == 0:
					toFlip += i
					moves += 1
					multOfK = True
					break
			if not multOfK:
				toFlip += ableMove[0]
				moves += 1
		print('found')
		moves += toFlip / K
		return moves



bf = BinaryFlips()
A = int(input())
B = int(input())
K = int(input())
print(bf.minimalMoves(A, B, K))
