from collections import deque
import sys
input = sys.stdin.readline


def topology_sort():
    # bfs, indegree
    ans = []

    qu = deque()
    for i, v in enumerate(indegree):
        if v == 0:
            qu.append(i)
            ans.append(i)

    while qu:
        now = qu.popleft()
        for end in graph[now]:
            indegree[end] -= 1
            if indegree[end] == 0:
                qu.append(end)
                ans.append(end)
    return ans


N, M = map(int, input().split())
indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1
    graph[A].append(B)


ans = topology_sort()


print(*ans[1:])
