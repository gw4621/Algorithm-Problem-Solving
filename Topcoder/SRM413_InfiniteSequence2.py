class InfiniteSequence2:
	def calc(self, n, p, q, x, y):
		if n <= 0:
			return 1
		queue = [n]
		dicA = {}
		while queue:
			print(queue)
			num = queue[0]
			first = num//p - x
			second = num//q - y
			delAble = True
			if first > 0 and first not in dicA:
				delAble = False
				queue.insert(0, first)
			if second > 0 and second not in dicA:
				delAble = False
				queue.insert(0, second)
			if delAble:
				if first <= 0:
					firstVal = 1
				else:
					firstVal = dicA[first]
				if second <= 0:
					secondVal = 1
				else:
					secondVal = dicA[second]
				dicA[num] = firstVal + secondVal
				del queue[0]
		return dicA[n]

infSeq = InfiniteSequence2()
n = int(input())
p = int(input())
q = int(input())
x = int(input())
y = int(input())
print(infSeq.calc(n, p, q, x, y))
