from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)


def bfs(v, visited):
    cnt = 0
    qu = deque()
    qu.append(v)
    visited[v] = True

    while qu:
        parent = qu.popleft()
        for child in graph[parent]:
            if not visited[child]:
                qu.append(child)
                visited[child] = True
                cnt += 1
    return cnt


dist = [0 for _ in range(N+1)]

for i in range(1, N+1):
    cnt = bfs(i, [False for _ in range(N+1)])
    dist[i] = cnt


max_num = max(dist)
for i, v in enumerate(dist):
    if v == max_num:
        print(i, end=' ')
