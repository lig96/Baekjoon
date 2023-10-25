
import sys
input = sys.stdin.readline


V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-2, 2):
        graph[temp[0]].append((temp[i], temp[i+1]))


def dfs(v, dist, far):
    visited[v] = True

    for node in graph[v]:
        if not visited[node[0]]:
            dfs(node[0], dist+node[1], far)

    if dist > far[1]:
        far[0] = v
        far[1] = dist


start = 1
visited = [False for _ in range(V+1)]
far_v1 = [-1, -1]
dfs(start, 0, far_v1)
# from 1 to far_v1[0], dist = far_v1[1]
visited = [False for _ in range(V+1)]
far_v2 = [-1, -1]
dfs(far_v1[0], 0, far_v2)
# from far_v1[0] to far_v2[0], dist = far_v2[1]


print(far_v2[1])
