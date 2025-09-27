# vy를 갖는 직선
# hy = root(vy**2 - width**2)
# y = hy/width * x
#
# vx를 갖는 직선
# hx = root(vx**2 - width**2)
# y = -hx/width * x + hx
#
# 두 직선의 교점
# (hy/width + hx/width) * x = hx
# {(hy + hx)/width} * x = hx
# x = hx / {(hy + hx) / width}
# x = hx / (hy + hx) * width
# 이 x가 교점의 x 좌표이다.
#
# y = hy/width * {hx / (hy + hx) * width}
# 이 y가 교점의 y 좌표이다.
#
# 이 y가 c가 되게끔하는 width를 구하면 된다.


import sys
input = sys.stdin.readline


def bisect_left(vx, vy, vc, lo, hi):
    def intersection_y():
        def hy():
            return (vy**2 - mid**2)**0.5

        def hx():
            return (vx**2 - mid**2)**0.5

        # y = hy/width * {hx / (hy + hx) * width}
        ret = hy() * hx() / (hy()+hx())
        # print(ret, vx, vy, mid)
        return ret

    for _ in range(200):
        mid = (lo+hi)/2
        if mid > min(vx, vy):
            # 지나치게 width가 커서 교점이 아예 없는 경우
            hi = mid
            continue
        if intersection_y() <= vc:
            hi = mid
        else:
            lo = mid
    return lo


x, y, c = map(float, input().split())


vx, vy, vc = x, y, c


ans = bisect_left(vx, vy, vc, lo=0, hi=3_000_000_000+1)


print(ans)
