from collections import defaultdict

def checkRight(line):
	stack = []
	for ch in line:
		if ch == '(' or ch == '[':
			stack.append(ch)
		elif ch == ')':
			if stack and stack[-1] == '(':
				stack.pop()
			else:
				return False
		elif ch == ']':
			if stack and stack[-1] == '[':
				stack.pop()
			else:
				return False
	if stack:
		return False
	return True

def solve(line):
	if not checkRight(line):
		return 0
	layerSum = defaultdict(lambda : 0)
	layer = 0
	for  ch in line:
		if ch == '(':
			layer += 1
		elif ch == ')':
			layer -= 1
			if layerSum[layer+1] > 0:
				layerSum[layer] += layerSum[layer+1] * 2
				layerSum[layer+1] = 0
			else:
				layerSum[layer] += 2
		elif ch == '[':
			layer += 1
		elif ch == ']':
			layer -= 1
			if layerSum[layer+1] > 0:
				layerSum[layer] += layerSum[layer+1] * 3
				layerSum[layer+1] = 0
			else:
				layerSum[layer] += 3
		#print(f'Layer: {layer}, sum: {list(layerSum.items())}')
	return layerSum[0]
			
			
	

line = input()
print(solve(line))