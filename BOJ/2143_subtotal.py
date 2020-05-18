import bisect
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
Asub = []
Bsub = []
for i in range(n):
	tmp = A[i]
	Asub.append(tmp)
	for j in range(i+1, n):
		tmp += A[j]
		Asub.append(tmp)
for i in range(m):
	tmp = B[i]
	Bsub.append(tmp)
	for j in range(i+1, m):
		tmp += B[j]
		Bsub.append(tmp)
Asub.sort()
answer = 0
for i in Bsub:
	answer += bisect.bisect_right(Asub, T-i) - bisect.bisect_left(Asub, T-i)
print(answer)