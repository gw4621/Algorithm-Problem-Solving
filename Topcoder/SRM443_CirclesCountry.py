class CirclesCountry:
	def leastBorders(self, X, Y, R, x1, y1, x2, y2):
		numOfCircle = len(X)
		border = 0
		for i in range(numOfCircle):
			if ((X[i]-x1)**2 + (Y[i]-y1)**2 < R[i]**2 and (X[i]-x2)**2 + (Y[i]-y2)**2 > R[i]**2) or ((X[i]-x1)**2 + (Y[i]-y1)**2 > R[i]**2 and (X[i]-x2)**2 + (Y[i]-y2)**2 < R[i]**2):
				border += 1
		return border

cc = CirclesCountry()
X = list(map(int, input().split(', ')))
Y = list(map(int, input().split(', ')))
R = list(map(int, input().split(', ')))
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(cc.leastBorders(X, Y, R, x1, y1, x2, y2))
