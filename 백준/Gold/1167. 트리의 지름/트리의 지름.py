import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)+100)


def dfs(graph, startx, startc):
    visited[startx] = startc
    for nxt, nxt_c in graph[startx]:
        if visited[nxt] != -1:
            continue
        dfs(graph, nxt, visited[startx]+nxt_c)
    return


def find():
    max_dist = max(visited)
    v = visited.index(max_dist)
    return v, max_dist


V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    temp = list(map(int, input().split()))
    s = temp[0]
    for i in range(1, len(temp)-1, 2):
        e, c = temp[i], temp[i+1]
        graph[s].append((e, c))


startx = 1
visited = [-1 for _ in range(V+1)]
dfs(graph, startx, 0)
endx, _ = find()
# from 1 to a, dist = _
startx = endx
visited = [-1 for _ in range(V+1)]
dfs(graph, startx, 0)
_, diameter = find()
# from a to b, dist = diameter


print(diameter)
