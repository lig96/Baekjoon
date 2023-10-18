
from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    ai, bi = map(int, input().split())
    graph[ai].append(bi)
    graph[bi].append(ai)


def bfs(graph, v, visited):
    qu = deque()
    qu.append((0, v))
    visited[v] = 0

    while qu:
        now_depth, now = qu.popleft()
        for end in graph[now]:
            if visited[end] == -1:
                qu.append((now_depth+1, end))
                visited[end] = now_depth+1


visited = [-1 for _ in range(N+1)]
bfs(graph, 1, visited)


max_num = max(visited)
print(visited.index(max_num), max_num, visited.count(max_num))