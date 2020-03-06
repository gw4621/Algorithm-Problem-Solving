import operator

class BatchSystem:
	def schedule(self, duration, user):
		tasklen = len(duration)
		task = [[i, duration[i], user[i]] for i in range(tasklen)]
		sortedTask = sorted(task, key=operator.itemgetter(1))
		print(sortedTask)
		for _ in range(tasklen-1):
			for i in range(tasklen-1):
				if sortedTask[i][1] == sortedTask[i+1][1]:	# If duration is same
					if sortedTask[i][2] > sortedTask[i+1][2]:
						tmp = sortedTask[i][:]
						sortedTask[i] = sortedTask[i+1][:]
						sortedTask[i+1] = tmp[:]
					elif sortedTask[i][2] == sortedTask[i+1][2] and sortedTask[i][0] > sortedTask[i+1][1]:
						tmp = sortedTask[i][:]
						sortedTask[i] = sortedTask[i+1][:]
						sortedTask[i+1] = tmp[:]
		return [sortedTask[i][0] for i in range(tasklen)]

bs = BatchSystem()
inpstr = input()
duration = list(map(int, inpstr.split(', ')))
inpstr = input()
user = inpstr.split(', ')
print(bs.schedule(duration, user))
