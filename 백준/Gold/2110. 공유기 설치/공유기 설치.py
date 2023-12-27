from bisect import bisect_left
import sys
input = sys.stdin.readline


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]


houses.sort()
min_gap = 1
max_gap = (houses[-1]-houses[0])//(C-1)


gap = max_gap
while True:
    now_i = 0
    is_broken = False

    for _ in range(C-1):
        # 1개는 무조건 cs[0]에.
        # C-1개를 배치시키는 것이니
        now = houses[now_i]
        next_target = now+gap
        next_i = bisect_left(houses, next_target)
        if next_i == len(houses):
            is_broken = True
            break
        else:
            now_i = next_i

    if is_broken:
        # 간격을 줄여야 됨
        gap, max_gap = (min_gap+gap)//2, gap
    else:
        # 간격을 늘려야 됨
        gap, min_gap = (gap+max_gap)//2, gap

    if (gap == min_gap) or (gap == max_gap):
        break


print(gap)
