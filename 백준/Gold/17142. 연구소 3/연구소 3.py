# 비활성 바이러스 역시 바이러스라서 이미 퍼트린 걸로 간주된다.
# 따라서 그 비활성 바이러스가 감염된 시간은 제외하고
# 오로지 빈 방이 감염된 시간만 나중에 계산하면 된다.


import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline


def combinations_(iterable, r):
    def combinations__(iterable, start_i, r, ret):
        if len(ret) == r:
            yield ret
        else:
            for i in range(start_i, len(iterable)):
                v = iterable[i]
                ret.append(v)
                yield from combinations__(iterable, start_i+1, r, ret)
                ret.pop()

    yield from combinations__(iterable, 0, r, [])


def bfs(rcs):
    dq = deque()
    for rc in rcs:
        r, c = rc
        dq.append((r, c, 0))
        visited[r][c] = 0

    while dq:
        r, c, d = dq.popleft()
        for i in range(4):
            newr, newc, newd = r+dr[i], c+dc[i], d+1
            if not (0 <= newr < N and 0 <= newc < N):
                continue
            if board[newr][newc] == "1":
                # 벽
                continue
            if visited[newr][newc] is not None:
                # 이미 방문함
                continue
            dq.append((newr, newc, newd))
            visited[newr][newc] = newd

    return visited


def max_time():
    for r in range(N):
        for c in range(N):
            if board[r][c] == "0" and visited[r][c] is None:
                # 하나라도 빈 공간이 미방문이라면
                return float('inf')

    # if not any(board[r][c] == "0" for r in range(N) for c in range(N)):
    #     # 빈 방이 애초부터 하나도 없으면
    #     return 0
    # temp_max = -float('inf')
    # # 이렇게 해도 되고 그냥 temp_max = 0으로 해도 된다.

    temp_max = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == "0":
                temp_max = max(temp_max, visited[r][c])
    return temp_max


N, M = map(int, input().split())
board: list[list[str]] = [list(map(str, input().split())) for _ in range(N)]


viruses = [(r, c) for r in range(N) for c in range(N)
           if board[r][c] == "2"]
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


supremum = float('inf')
for chosen_viruses in combinations(viruses, M):
    visited = [[None for _ in range(N)] for _ in range(N)]
    # visited[r][c] = 방문 여부 겸 닿는 시간
    bfs(chosen_viruses)
    supremum = min(supremum, max_time())


print(supremum if supremum != float('inf') else -1)
