import sys

def solve(N, S):
	if N == 1:
		return S[0]
	elif N == 2:
		return S[0] + S[1]
	score = [0 for _ in range(N)]
	score[0] = S[0]
	score[1] = S[0] + S[1]
	score[2] = max(S[0] + S[2], S[1] + S[2])
	for i in range(3, N):
		score[i] = max(score[i-3] + S[i] + S[i-1], score[i-2] + S[i])
	return score[N-1]

N = int(sys.stdin.readline())
S = []
for _ in range(N):
	S.append(int(sys.stdin.readline()))
print(solve(N, S))