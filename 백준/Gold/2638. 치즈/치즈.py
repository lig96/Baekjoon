
from collections import deque


def bfs(r, c):
    qu = deque()
    qu.append((r, c))
    visited[r][c] += 1
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 1:
                    # 치즈라면
                    # 방문이 무엇이든 상관없이
                    visited[nr][nc] += 1
                else:
                    # 공기라면
                    # 방문이 0이라면
                    if not visited[nr][nc]:
                        visited[nr][nc] += 1
                        qu.append((nr, nc))
    return


def do_melt():
    flag = False
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 1 and visited[r][c] >= 2:
                graph[r][c] = 0
                flag = True
    return flag


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
ans = 0
while True:
    visited = [[0 for _ in range(M)]for _ in range(N)]

    bfs(0, 0)
    flag = do_melt()
    if flag:
        ans += 1
    else:
        break


print(ans)
