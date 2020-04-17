UP, RIGHT, LEFT, DOWN = 0, 1, 2, 3
dr = (-1, 0, 0, 1)
dc = (0, 1, -1, 0)

def simulate(board, wormhole, startR, startC, d):
    r, c = startR, startC
    if board[r][c] != 0:
        return 0
    score = 0
    while True:
        r += dr[d]
        c += dc[d]
        if board[r][c] == 0:
            if r == startR and c == startC:
                return score
        elif board[r][c] == 1 and (d == LEFT or d == DOWN):	# DOWN->RIGHT, LEFT->UP
            d -= 2
            score += 1
        elif board[r][c] == 2 and (d == UP or d == LEFT):	# LEFT->DOWN, UP->RIGHT
            d ^= 1
            score += 1
        elif board[r][c] == 3 and (d == RIGHT or d == UP):	# RIGHT->DOWN, UP->LEFT
            d ^= 2
            score += 1
        elif board[r][c] == 4 and (d == DOWN or d == RIGHT):	# DOWN->LEFT, RIGHT->UP
            d -= 1
            score += 1
        elif board[r][c] > 0 and board[r][c] <= 5:
            d = 3 - d
            score += 1
        elif board[r][c] > 5:
            r, c = wormhole[(r, c)]
        else:
            return score
        

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    wormList = [-1 for _ in range(5)]
    wormDict = {}
    board = [[5 for _ in range(N+2)]]
    for i in range(1, N+1):
        board.append([5] + list(map(int, input().split())) + [5])
        for j in range(1, N+1):
            if board[i][j] > 5:
                if wormList[board[i][j]-6] == -1:
                    wormList[board[i][j]-6] = (i, j)
                else:
                    tmp = wormList[board[i][j] - 6]
                    wormDict[(i, j)] = tmp
                    wormDict[tmp] = (i, j)
    board.append([5 for _ in range(N+2)])
    maxScore = 0
    for d in range(4):
        for r in range(1, N+1):
            for c in range(1, N+1):
                nextR, nextC = r+dr[d], c+dc[d]
                if board[r][c] == 0 and board[nextR][nextC] != 0:
                    maxScore = max(maxScore, simulate(board, wormDict, r, c, d))
    print(f'#{test_case} {maxScore}')
