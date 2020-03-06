class ColorfulBoxesAndBalls:
	def getMaximum(self, numRed, numBlue, onlyRed, onlyBlue, bothColors):
		maxWrongColor = min(numRed, numBlue)
		scores = []
		for i in range(0, maxWrongColor+1):
			scores.append(onlyRed*(numRed-i) + onlyBlue*(numBlue-i) + bothColors*(i*2))
		return max(scores)

cbab = ColorfulBoxesAndBalls()
numRed = int(input())
numBlue = int(input())
onlyRed = int(input())
onlyBlue = int(input())
bothColors = int(input())
print(cbab.getMaximum(numRed, numBlue, onlyRed, onlyBlue, bothColors))
