# visited의 초깃값을 -1로 두면
# -1이란 값이 미방문이 아니라 t = -1로 해석되어서 주의해야 한다.
# INF로 놓거나 별개의 None으로 둬야 한다.


from collections import deque
import sys
input = sys.stdin.readline


def bfs(board, R, C, start_pos, restriction):
    dq = deque(start_pos)
    visited = [[None for _ in range(C)] for _ in range(R)]
    for r, c, t in dq:
        visited[r][c] = t

    while dq:
        r, c, t = dq.popleft()
        for i in range(4):
            newr, newc, newt = r+dr[i], c+dc[i], t+1
            if not (0 <= newr < R and 0 <= newc < C):
                continue
            if board[newr][newc] == "#":
                continue
            if visited[newr][newc] != None:
                continue
            if (
                (restriction is not None)
                and (restriction[newr][newc] is not None)
                and (restriction[newr][newc] <= newt)
            ):
                continue
            visited[newr][newc] = newt
            dq.append((newr, newc, newt))
    return visited


R, C = list(map(int, input().split()))
board = [list(input().rstrip()) for _ in range(R)]
# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간
# J는 입력에서 하나만 주어진다.


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
fire_pos = [(r, c, 0)
            for r in range(R) for c in range(C)
            if board[r][c] == "F"]
human_pos = [(r, c, 0)
             for r in range(R) for c in range(C)
             if board[r][c] == "J"]


fire_visited = bfs(board, R, C, fire_pos, None)
human_visited = bfs(board, R, C, human_pos, fire_visited)


ans = float('inf')
for r in (0, R-1):
    for c in range(C):
        if human_visited[r][c] is None:
            continue
        ans = min(ans, human_visited[r][c])
for r in range(R):
    for c in (0, C-1):
        if human_visited[r][c] is None:
            continue
        ans = min(ans, human_visited[r][c])


print(ans+1 if ans != float('inf') else "IMPOSSIBLE")
