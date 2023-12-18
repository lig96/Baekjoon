import sys
input = sys.stdin.readline


def make_dist_arr(N, stars):
    dist_arr = []
    # dist, left_i, right_i
    for xyz in range(3):
        # x 혹은 y 혹은 z
        temp = sorted(stars, key=lambda x: x[xyz])
        for i in range(N-1):
            left = temp[i]
            right = temp[i+1]

            dist = right[xyz] - left[xyz]
            left_i = left[3]
            right_i = right[3]

            dist_arr.append((dist, left_i, right_i))
    return sorted(dist_arr, key=lambda x: x[0])


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


def sol():
    ans = 0
    for dist, a, b in dist_arr:
        if find(a) != find(b):
            union(a, b)
            ans += dist
    return ans


N = int(input())
stars = [list(map(int, input().split()))+[i] for i in range(N)]
# stars[ind] = x, y, z, ind


dist_arr = make_dist_arr(N, stars)
parent = [i for i in range(N)]


print(sol())