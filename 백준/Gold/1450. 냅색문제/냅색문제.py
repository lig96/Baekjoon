import sys
input = sys.stdin.readline


# def make_subset_sums(start, end):
#     def dfs(now, ret_v):
#         if now == end:
#             ret.append(ret_v)
#             return
#         for i in range(2):
#             dfs(now+1, ret_v + weights[now]*i)
#         return
#     ret = []
#     dfs(start, 0)
#     return ret


def make_subset_sums(start, end):
    ret = [0]
    for i in range(start, end):
        v = weights[i]
        ret.extend([(x+v) for x in ret])
    return ret


def bisect_right(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] <= x:
            lo = mid+1
        else:
            hi = mid
    return lo


N, C = map(int, input().split())
weights = list(map(int, input().split()))


left_arr = make_subset_sums(0, N//2)
right_arr = make_subset_sums(N//2, N)
left_arr.sort(reverse=True)
right_arr.sort()


ans = 0
lo = 0
for v in left_arr:
    lo = bisect_right(a=right_arr, x=C-v, lo=lo)
    ans += lo


print(ans)
