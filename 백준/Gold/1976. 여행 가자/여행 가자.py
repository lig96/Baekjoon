import sys
input = sys.stdin.readline


def floyd_warshall():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                graph[i][j] = INF
            if i == j:
                graph[i][j] = 0
    for mid in range(N):
        for s in range(N):
            for e in range(N):
                graph[s][e] = min(graph[s][e],
                                  graph[s][mid]+graph[mid][e])
    return


N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x: int(x)-1, input().split()))
# 0-indexing


INF = float('inf')
floyd_warshall()


tot_cost = 0
for i in range(M-1):
    now, nxt = plan[i], plan[i+1]
    tot_cost += graph[now][nxt]


print('YES' if tot_cost != INF else 'NO')
