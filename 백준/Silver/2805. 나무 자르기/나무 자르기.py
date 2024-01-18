import sys
input = sys.stdin.readline


def bisect_right(lo, hi, target):
    while lo < hi:
        mid = (lo+hi)//2
        if cut(mid) < target:
            hi = mid
        else:
            lo = mid+1
    return lo


def cut(H):
    ret = 0
    for tree in trees:
        if tree >= H:
            ret += tree-H
    return ret


N, M = map(int, input().split())
trees = list(map(int, input().split()))


ans = bisect_right(lo=0, hi=1_000_000_000+1, target=M)
# 1<=M이기 때문에 hi에 1을 안 더해도 정답 처리됨


print(ans-1)
