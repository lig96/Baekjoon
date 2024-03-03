import sys
input = sys.stdin.readline


def union(a, b):
    a, b = find(a), find(b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b
    return


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


N = int(input())
M = int(input())
infos = [list(map(int, input().split())) for _ in range(M)]


infos.sort(key=lambda x: x[2])
parent = [i for i in range(N+1)]


ans = 0
for a, b, c in infos:
    if find(a) != find(b):
        union(a, b)
        ans += c


print(ans)
