N = int(input())
if N == 1:
	print(0)
else:
	isPrime = [True for _ in range(N+1)]
	isPrime[0] = False
	isPrime[1] = False
	primes = []
	for i in range(2, N+1):
		if isPrime[i]:
			primes.append(i)
			num = i << 1
			while num <= N:
				isPrime[num] = False
				num += i
	answer = 0
	start = 0
	end = 1
	total = primes[0]
	while start < len(primes):
		if total == N:
			answer += 1
			total -= primes[start]
			start += 1
		elif total > N:
			total -= primes[start]
			start += 1
		elif total < N:
			if end == len(primes):
				break
			total += primes[end]
			end += 1
	print(answer)