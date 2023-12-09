import sys
input = sys.stdin.readline


def dfs(start):
    if sum(visited) == N:
        if graph[start][0] != 0:
            return graph[start][0]
        else:
            return float('inf')

    visited[start] = True

    min_dist = float('inf')
    for end in range(N):
        if visited[end]:
            # 이미 방문한 경우
            continue
        if graph[start][end] == 0:
            # 방문할 수 없는 경우
            continue
        visited[end] = True
        temp = dfs(end) + graph[start][end]
        visited[end] = False
        if min_dist > temp:
            min_dist = temp
    return min_dist


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# graph[start][end] = cost


visited = [False for _ in range(N)]


print(dfs(0))
