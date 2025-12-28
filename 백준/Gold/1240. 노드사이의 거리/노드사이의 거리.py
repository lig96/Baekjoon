import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def dfs(graph, N, x):
    INF = float('inf')
    visited = [INF for _ in range(N+1)]
    stack = []
    visited[x] = 0
    stack.append(x)
    while stack:
        x = stack.pop()
        for child, dist in graph[x]:
            if visited[child] == INF:
                visited[child] = visited[x]+dist
                stack.append(child)
    return visited


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]  # 원인덱싱
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
node_pairs = [list(map(int, input().split())) for _ in range(M)]


dists = []
for x in range(N+1):
    temp = dfs(graph, N, x)
    dists.append(temp)


for a, b in node_pairs:
    sys_print(str(dists[a][b])+'\n')
