class NumberMagicEasy:
	def theNumber(self, answer):
		result = set([i for i in range(1, 17)])
		card = [set([1, 2, 3, 4, 5, 6, 7, 8]), set([1, 2, 3, 4, 9, 10, 11, 12]), set([1, 2, 5, 6, 9, 10, 13, 14]), set([1, 3, 5, 7, 9, 11, 13, 15])]
		for i in range(4):
			if answer[i].lower() == 'y':
				result &= card[i]
			else:
				result -= card[i]
		return tuple(result)[0]
nme = NumberMagicEasy()
print(nme.theNumber(input()))
