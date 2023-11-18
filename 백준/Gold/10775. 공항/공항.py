import sys
input = sys.stdin.readline


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


G = int(input())
P = int(input())
landings = [int(input()) for _ in range(P)]


parent = [i for i in range(G+1)]
for i, landing in enumerate(landings):
    can_gate = find(landing)
    if can_gate != 0:
        union(can_gate, can_gate-1)
    else:
        print(i)
        break
else:
    print(i+1)
