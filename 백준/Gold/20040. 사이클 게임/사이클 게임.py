import sys
input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [x for x in range(n)]
for i in range(m):
    s, e = map(int, input().split())
    if find(s) != find(e):
        union(s, e)
    else:
        print(i+1)
        break
else:
    print(0)
