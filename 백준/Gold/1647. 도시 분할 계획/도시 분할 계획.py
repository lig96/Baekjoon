# 0942


import sys
input = sys.stdin.readline


def kruskal():
    ans, before = 0, 0
    for start, end, c in graph:
        if find(start) != find(end):
            union(start, end)
            ans, before = ans+before, c
    # 맨 마지막 c 대신 맨 처음에 before0이 대입
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
graph = [tuple(map(int, input().split())) for _ in range(M)]


graph.sort(key=lambda x: x[2])
parent = [x for x in range(N+1)]


print(kruskal())
