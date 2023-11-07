
import sys
input = sys.stdin.readline


def kruskal():
    ans = []
    for start, end, c in graph:
        if find(start) != find(end):
            union(start, end)
            ans.append(c)
    ans.pop()
    return ans


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]


graph.sort(key=lambda x: x[2])
parent = [x for x in range(N+1)]


ans = kruskal()


print(sum(ans))
