def makeCombinations(It, n):
	listIt = list(It)
	Itlen = len(listIt)
	stack = [([], 0)]
	done = []
	while len(stack) > 0:
		c, idx = stack.pop()
		clen = len(c)
		if clen == n:
			done.append(c)
		elif n-clen == Itlen - idx:
			done.append(c+listIt[idx:])
		else:
			stack.append((c, idx+1))
			stack.append((c+[listIt[idx]], idx+1))
	return done

if __name__ == "__main__":
	print(makeCombinations(range(6), 3))