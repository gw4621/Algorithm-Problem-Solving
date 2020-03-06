class StockHistory:
	def maximumEarnings(self, initialInvestment, monthlyContribution, stockPrices):
		totalMonth = len(stockPrices)
		sPrices = []
		for i in range(totalMonth):
			sPrices.append(list(map(int, stockPrices[i].split())))
		numOfStocks = len(sPrices[0])
		earning = 0
		maxRate = 1
		fsp = sPrices[-1][:] # Final Stock Price
		for i in range(totalMonth-2, -1, -1):
			for j in range(numOfStocks):
				if fsp[j] / sPrices[i][j] > maxRate:
					maxRate = fsp[j] / sPrices[i][j]
			earning += (maxRate - 1) * monthlyContribution
		earning += (maxRate - 1) * (initialInvestment - monthlyContribution)
		return round(earning)



sh = StockHistory()
initialInvestment = int(input())
monthlyContribution = int(input())
stockPrices = []
inpstr = input()
while inpstr != '':
	stockPrices.append(inpstr)
	inpstr = input()
print(sh.maximumEarnings(initialInvestment, monthlyContribution, stockPrices))
