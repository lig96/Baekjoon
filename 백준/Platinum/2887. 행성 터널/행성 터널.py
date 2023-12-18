# mst를 구현하면 된다.
# 하지만 n이 크기 때문에 모든 경우의 수,
# 즉 nC2, n^2개의 거리(인접 행렬 형태)를 구할 순 없다.

# x축으로 이동하는 게 최단 거리일 때만 거리를 구해보자.
# x좌표로 오름차순 정렬 후 바로 오른쪽 행성과의 거리만 구한다.
# 1-2, 2-3만 구하고 1-3, 1-4 등은 안 구해도 되는 이유는
# 경로 1-2, 2-3과 경로 1-3은 총합 거리는 같지만
# 전자가 연결된 행성의 개수가 더 많기 때문이다.
# 정렬 nlogn, 순회 n이다.
# 이것을 x축, y축, z축일 때 반복하니 곱하기 3을 해준다.
# O(3*(nlogn + n))

# 이렇게 구한 dist_arr을 정렬 후 크루스칼 알고리즘을 시행한다.
# 정렬 3nlog3n, 순회 3n, union-find ?이다.
# O(3nlog3n + 3n*?)

# 종합
# O(nlogn + n*unionfind)


import sys
input = sys.stdin.readline


def make_dist_arr(N, stars):
    arr = []
    # dist, left_i, right_i

    for xyz in range(3):
        stars.sort(key=lambda x: x[xyz])
        # 메모리 절약을 위해 stars 자체를 변경
        for i in range(N-1):
            l = stars[i]
            r = stars[i+1]
            arr.append((r[xyz] - l[xyz], l[3], r[3]))

    return arr


def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    return


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def kruskal():
    dist_arr.sort(key=lambda x: x[0])
    ans = 0

    for dist, a, b in dist_arr:
        if find(a) != find(b):
            union(a, b)
            ans += dist

    return ans


N = int(input())
stars = [list(map(int, input().split()))+[i] for i in range(N)]
# x, y, z, index


dist_arr = make_dist_arr(N, stars)
parent = [i for i in range(N)]


ans = kruskal()


print(ans)
