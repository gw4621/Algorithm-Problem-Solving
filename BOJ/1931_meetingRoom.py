import sys
input = sys.stdin.readline
N = int(input())
M = []
for _ in range(N):
	M.append(tuple(map(int, input().split())))
M = sorted(M)
num = 1
end = float('inf')
for i in M:
	if i[1] < end:
		end = i[1]
	elif i[0] == end and i[1] == end:
		num += 1
	elif i[1] > end:
		if i[0] >= end:
			end = i[1]
			num += 1
print(num)