import sys
input = sys.stdin.readline


def trisect(lo, hi):
    for _ in range(200):
        llr = lo*0.55 + hi*0.45
        lrr = lo*0.45 + hi*0.55

        dot_a_llr = find_loc(As, Ae, llr)
        dot_b_llr = find_loc(Bs, Be, llr)
        dot_a_lrr = find_loc(As, Ae, lrr)
        dot_b_lrr = find_loc(Bs, Be, lrr)

        dist_llr = dist(dot_a_llr, dot_b_llr)
        dist_lrr = dist(dot_a_lrr, dot_b_lrr)

        if dist_llr <= dist_lrr:
            hi = lrr
        else:
            lo = llr
    return dist_llr


def find_loc(start, end, p):
    ret_x = start[0]*(1-p)+end[0]*(p)
    ret_y = start[1]*(1-p)+end[1]*(p)
    return (ret_x, ret_y)


def dist(a, b):
    return ((b[0]-a[0])**2 + (b[1]-a[1])**2)**(1/2)


Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())
As = (Ax, Ay)  # A start
Ae = (Bx, By)  # A end
Bs = (Cx, Cy)  # B start
Be = (Dx, Dy)  # B end


ans = trisect(lo=0, hi=1)


print(ans)
