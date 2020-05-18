import sys

input = sys.stdin.readline

def gcd(a, b):
	if a < b:
		tmp = a
		a = b
		b = tmp
	while b != 0:
		tmp = a % b
		a = b
		b = tmp
	return a
	
def solve(a, b):
	s = [1, 0]
	t = [0, 1]
	r = [a, b]
	q = [0]
	while True:
		q.append(r[-2] // r[-1])
		r.append(r[-2] - r[-1]*q[-1])
		if r[-1] == 0:
			while t[-1] < 0 or b * t[-1] <= 1:
				t[-1] += a
			return t[-1]
		s.append(s[-2]-s[-1]*q[-1])
		t.append(t[-2]-t[-1]*q[-1])

t = int(input())
for _ in range(t):
	K, C = map(int, input().split())
	if gcd(K, C) != 1:
		print('IMPOSSIBLE')
	else:
		ans = solve(K, C)
		if ans <= 1000000000:
			print(ans)
		else:
			print('IMPOSSIBLE')