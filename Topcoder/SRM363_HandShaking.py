class HandShaking:
	def countPerfect(self, n):
		if n % 2 > 0:
			return 0
		cp = [1]
		goalN = n/2 - 1
		n = 0
		while n < goalN:
			n += 1
			nextCP = cp[-1] * 2
			i = n - 2
			j = 0
			while i >= 0:
				nextCP += cp[i] * cp[j]
				i -= 1
				j += 1
			cp.append(nextCP)
		return cp[-1]

hs = HandShaking()
print(hs.countPerfect(int(input())))
