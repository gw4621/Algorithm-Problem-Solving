import math
import decimal

def calcRate(X, Y):
	return (Y*100) // X

def solve(X, Y):
	rate = calcRate(X, Y)
	if rate >= 99:
		return -1
	a = decimal.Decimal(Y) / decimal.Decimal(X)
	b = (1+rate-(100*a)) / (decimal.Decimal(99) - rate)
	ans1 = math.floor(b*X)
	if calcRate(X+ans1, Y+ans1) == rate+1:
		return ans1
	else:
		return math.ceil(b*X)

while True:
	try:
		X, Y = map(int, input().split())
		print(solve(X, Y))
	except EOFError:
		break