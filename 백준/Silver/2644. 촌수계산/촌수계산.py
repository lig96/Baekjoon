import sys
input = sys.stdin.readline


def dfs(graph, start):
    visited[start] = 0
    stack = list([start])

    while stack:
        now = stack.pop()
        for end in graph[now]:
            if visited[end] == -1:
                visited[end] = visited[now]+1
                stack.append(end)
    return


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)


visited = [-1 for _ in range(n+1)]
dfs(graph, a)


print(visited[b])
