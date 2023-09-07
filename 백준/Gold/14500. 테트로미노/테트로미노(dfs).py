import sys
input = sys.stdin.readline


def dfs(v, idx, total):
    global ans

    r, c = v
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return

    for i in range(3):
        # 4번째는 이미 그 전에 했던 것이라 중복
        newr, newc = r+dr[i], c+dc[i]
        if (0 <= newr < ROW) and (0 <= newc < COL) and (not visited[newr][newc]):
            if idx == 1:
                visited[newr][newc] = True
                dfs((r, c), idx+1, total+mat[newr][newc])
                visited[newr][newc] = False
            visited[newr][newc] = True
            dfs((newr, newc), idx+1, total+mat[newr][newc])
            visited[newr][newc] = False


ROW, COL = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(ROW)]
visited = [[False for _ in range(COL)] for _ in range(ROW)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
max_val = max(map(max, mat))
ans = 0


for r in range(ROW):
    for c in range(COL):
        visited[r][c] = True
        dfs((r, c), 0, mat[r][c])
        visited[r][c] = False


print(ans)
