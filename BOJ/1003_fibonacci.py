ans = [(1, 0), (0, 1), (1, 1), (1, 2)]

def getAnswer(N):
	if len(ans)-1 >= N:
		return ans[N]
	while len(ans)-1 < N:
		ans.append((ans[-1][0] + ans[-2][0], ans[-1][1] + ans[-2][1]))
	return ans[N]

T = int(input())
for _ in range(T):
	N = int(input())
	toPrint = getAnswer(N)
	print(str(toPrint[0]) + ' ' + str(toPrint[1]))