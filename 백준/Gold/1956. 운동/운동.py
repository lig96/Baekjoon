# x -> x를 0으로 초기화 안 하고 해도 되기는 한데
# 하는 게 정석인 듯


import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def fw():
    for v in range(V):
        dists[v][v] = 0

    for mid in range(V):
        for i in range(V):
            for j in range(V):
                dists[i][j] = min(dists[i][j], dists[i][mid]+dists[mid][j])

    return dists


V, E = map(int, input().split())
INF = float('inf')
dists = [[INF for _ in range(V)] for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    dists[a-1][b-1] = c  # zero indexing


fw()


min_v = INF
for i in range(V):
    for j in range(V):
        if i == j:
            continue
        min_v = min(min_v, dists[i][j]+dists[j][i])


print(min_v if min_v != INF else -1)
