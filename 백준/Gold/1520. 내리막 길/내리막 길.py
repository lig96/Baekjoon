import sys
input = sys.stdin.readline


def dfs(graph, r, c):
    global ans

    visited[r][c][1] = True

    if r == M-1 and c == N-1:
        visited[r][c][0] += 1
        return visited[r][c]

    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if not (0 <= newr < M and 0 <= newc < N):
            continue
        if not (graph[newr][newc] < graph[r][c]):
            continue

        if not visited[newr][newc][1]:
            # 탐색 안 해봄
            visited[r][c][0] += dfs(graph, newr, newc)[0]
        else:
            # 탐색 해봄
            visited[r][c][0] += visited[newr][newc][0]
    return visited[r][c]


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[[0, False] for _ in range(N)] for _ in range(M)]
# ways to visit (M, N) , is_visited
dfs(graph, 0, 0)


print(visited[0][0][0])
# for i in visited:
#     print(*i)
