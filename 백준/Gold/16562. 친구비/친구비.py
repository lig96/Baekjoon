import sys
sys.setrecursionlimit(10_000+99)
input = sys.stdin.readline


def union(a, b, min_price):
    a, b = find(a), find(b)
    if a <= b:
        parent[b] = a
        min_price[a] = min(min_price[a], min_price[b])
    else:
        parent[a] = b
        min_price[b] = min(min_price[a], min_price[b])
    return


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


N, M, k = map(int, input().split())
A_arr = list(map(int, input().split()))
vw_arr = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
# zero-indexing


parent = [i for i in range(N)]
min_price = A_arr[::]
for v, w in vw_arr:
    union(v, w, min_price)


ans = 0
already_friend = set()
for i in range(N):
    par = find(i)
    if par not in already_friend:
        ans += min_price[par]
        already_friend.add(par)


print(ans if ans <= k else "Oh no")
