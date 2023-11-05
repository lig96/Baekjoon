import sys
input = sys.stdin.readline


def kruskal():
    ans = 0
    for start, end, c in graph:
        if find(start) != find(end):
            union(start, end)
            ans += c
    return ans


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]


graph.sort(key=lambda x: x[2])
parent = [i for i in range(V+1)]  # 자기 자신


print(kruskal())
