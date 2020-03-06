class HamiltonPath:
	def factorial(self, num):
		if num == 0:
			return 1
		else:
			return num * self.factorial(num-1)

	def countPaths(self, roads):
		numOfCities = len(roads)
		clusters = []
		# Count Clusters
		for i in range(numOfCities):
			connectedRoads = 0
			clusterNum = -1
			for k in range(len(clusters)):
				if i in clusters[k]:
					clusterNum = k
					break
			for j in range(i+1, numOfCities):
				if clusterNum >= 0 and j in clusters[clusterNum]:
					return 0
				if roads[i][j].lower() == 'y':
					if clusterNum < 0:
						for k in range(len(clusters)):
							if j in clusters[k]:
								clusterNum = k
								break
					if clusterNum < 0:
						clusters.append(set([i, j]))
						clusterNum = len(clusters)-1
					else:
						clusters[clusterNum].update([i, j])
					connectedRoads += 1
			if connectedRoads > 2:
				return 0
			if clusterNum < 0:
				clusters.append(set([i]))
		result = self.factorial(len(clusters))
		print(clusters)
		for i in clusters:
			if len(i) > 1:
				result *= 2
		return result % 1000000007

hp = HamiltonPath()
roads = []
roads.append(input())
for _ in range(len(roads[0]) - 1):
	roads.append(input())
print(hp.countPaths(roads))
