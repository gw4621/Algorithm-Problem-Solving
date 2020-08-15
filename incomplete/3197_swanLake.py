import sys
from collections import deque


# icemelt는 큐 또는 리스트, (바뀌는 Row, 바뀌는 Col, 바뀔 번호)의 형식으로 넣는다.

# 1. swan 퍼뜨리면서 닿는 얼음을 nextbfs 큐에 넣는다. 맞닥뜨리는 얼음을 icemelt에 넣되, 바뀔 때 swan의 번호로 바뀌도록 한다.

# 2. 물(swan 아님)과 닿아있는 얼음을 찾아 icemelt 리스트에 물로 바뀌게 넣는다

# 3. icemelt를 진행하는데, 이 때 물로 바뀐 부분을 다시 백조로 바꿀 순 있지만 백조를 물로 바꿀 수는 없는 점에 유의

# =========================================================
# 차라리 백조로 바뀌는 부분을 bfs로 뒤에 넣자

# 1. 백조 퍼뜨리면서 닿는 얼음을 nextbfs로 넣는다

# 2. 물과 닿은 얼음을 icemelt set에 넣는다

# 3. icemelt 진행하는데, 얼음 옆에 얼음이 더 있으면 넣는다. set을 사용하는게 좋을듯하다

# 4. 백조가 닿은 얼음 넣었던 nextbfs 큐를 원래 사용하는 큐로 바꾸고 bfs 하는데, 값을 모두 백조 번호로 바꾸되 얼음을 만나면 다시 nextbfs로 넣는다.


input = sys.stdin.readline

WATER = 0
ICE = 1
SWAN1 = 2
SWAN2 = 3


R, C = map(int, input().split())

lake = []

area = [[-1 for _ in range(C)] for _ in range(R)]

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

swan = 2
for _ in range(R):
    lake.append(list(input().strip()))

for r in range(R):
    for c in range(C):

            