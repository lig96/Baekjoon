N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def dfs(i, visited):
    for index, value in enumerate(graph[i]):
        if (value == 1) and (not visited[index]):
            visited[index] = 1
            dfs(index, visited)


for i in range(N):
    visited = [0 for _ in range(N)]
    dfs(i, visited)
    print(*visited)