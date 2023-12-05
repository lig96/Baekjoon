import sys
input = sys.stdin.readline


def dfs(graph, r, c):
    visited[r][c] = 0

    if r == M-1 and c == N-1:
        visited[r][c] = 1
        return 1

    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if not (0 <= newr < M and 0 <= newc < N):
            continue
        if not (graph[newr][newc] < graph[r][c]):
            continue

        if visited[newr][newc] == -1:
            # 탐색 안 해봄
            visited[r][c] += dfs(graph, newr, newc)
        else:
            # 탐색 해봄
            visited[r][c] += visited[newr][newc]
    return visited[r][c]


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[-1 for _ in range(N)] for _ in range(M)]
# ways to visit (M, N) , is_visited
dfs(graph, 0, 0)


print(visited[0][0])
# print(visited[0][0][0])
