import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e4))


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]


edges.sort(key=lambda x: x[2])
parent = [i for i in range(V+1)]


ans = 0
for s, e, c in edges:
    if find(s) == find(e):
        continue
    union(s, e)
    ans += c


print(ans)
