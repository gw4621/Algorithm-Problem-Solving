import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

lake = []

area = [[-1 for _ in range(C)] for _ in range(R)]

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

dq = deque()

def solve(dq):
    minTime = float('inf')
    nextDq = deque()
    while dq or nextDq:
        # Do BFS for the time
        found = False
        # print("print")
        # for i in range(R):
        #     print(''.join(lake[i]))
        # print()

        while dq:
            r, c, t = dq.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if area[nr][nc] < 0:
                        area[nr][nc] = area[r][c]
                        if lake[nr][nc] == 'X':
                            nextDq.append((nr, nc, t+1))
                        elif lake[nr][nc] == '.':
                            dq.append((nr, nc, t))
                    else:
                        if lake[nr][nc] == 'X' and area[nr][nc] != area[r][c]:
                            minTime = min(minTime, t+1)
                            # print((area[nr][nc], area[r][c], nr, nc, t+1, 'X'))
                            found = True
                        elif lake[nr][nc] == '.' and area[nr][nc] != area[r][c]:
                            minTime = min(minTime, t)
                            # print((area[nr][nc], area[r][c], nr, nc, t, '.'))
                            found = True
        if found:
            print(minTime)
            return
        
        # Ice melt
        melt = []
        for r in range(R):
            for c in range(C):
                if lake[r][c] == 'X':
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < R and 0 <= nc < C and (lake[nr][nc] == '.' or lake[nr][nc] == 'L'):
                            melt.append((r, c))
                            continue
        for r, c in melt:
            lake[r][c] = '.'

        # Change queue and lake
        tmp = dq
        dq = nextDq
        nextDq = tmp

swan = 1
for i in range(R):
    lake.append(list(input().strip()))
    for j in range(C):
        if lake[i][j] == 'L':
            area[i][j] = swan
            swan += 1
            dq.append((i, j, 0))
            
solve(dq)