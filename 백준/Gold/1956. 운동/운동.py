# x -> x를 0으로 초기화 안 하고 해도 됨
# 오히려 이게 더 논리에 맞음


import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def fw():
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


min_v = min(dists[i][i] for i in range(V))


print(min_v if min_v != float('inf') else -1)
