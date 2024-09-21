import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(500*500)+100)


def dfs(r, c):
    visited[r][c] = 0
    # 도달 가능 여부는 모르지만
    # 덧셈의 항등원
    if (r, c) == (R-1, C-1):
        visited[r][c] += 1
        # 도달했으니 +1
        return visited[r][c]

    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if not (0 <= newr < R and 0 <= newc < C):
            continue
        if board[r][c] <= board[newr][newc]:
            continue

        if visited[newr][newc] == -1:
            visited[r][c] += dfs(newr, newc)
        else:
            visited[r][c] += visited[newr][newc]

    return visited[r][c]


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


visited = [[-1 for _ in range(C)] for _ in range(R)]
# -1이면 미방문,
# -1이 아니라면 방문이 가능하고 (R-1, C-1) 도달의 경우의 수
dfs(0, 0)


print(visited[0][0])
