def kruskal():
    ans = 0.0
    for c, s, e in cost_arr:
        if find(s) != find(e):
            ans += c
            union(s, e)
    return ans


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


n = int(input())
xys = [list(map(float, input().split())) for _ in range(n)]


cost_arr = []
for s in range(n):
    for e in range(s+1, n):
        x1, y1 = xys[s]
        x2, y2 = xys[e]
        c = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
        cost_arr.append((c, s, e))
cost_arr.sort()
parent = [i for i in range(n)]


print(kruskal())
