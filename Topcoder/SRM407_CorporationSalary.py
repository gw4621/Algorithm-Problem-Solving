class CorporationSalary:
	def totalSalary(self, relations):
		totalEmp = len(relations)
		eachSal = [0 for _ in range(totalEmp)]
		findStack = []
		while eachSal.count(0) > 0:
			if not findStack:
				findStack.append(eachSal.index(0))
			while findStack:
				empNum = findStack[-1]
				if relations[empNum].count('Y') == 0:
					eachSal[empNum] = 1
					findStack.pop()
					continue
				empSal = 0
				for i in range(totalEmp):
					if relations[empNum][i] == 'Y' and eachSal[i] > 0:
						empSal += eachSal[i]
					elif relations[empNum][i] == 'Y' and eachSal[i] == 0:
						findStack.append(i)
						break
				if findStack[-1] != empNum:
					continue
				eachSal[empNum] = empSal
				findStack.pop()
		return sum(eachSal)


relations = [input()]
for i in range(len(relations[0])-1):
	relations.append(input())

cs = CorporationSalary()
print(cs.totalSalary(relations))
