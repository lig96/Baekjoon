import sys
input = sys.stdin.readline


def sol(points):
    def ccw(a, b, c):
        x1, y1 = a
        x2, y2 = b
        x3, y3 = c

        # vector1 = a->b = (x2-x1, y2-y1, 0)
        # vector2 = a->c = (x3-x1, y3-y1, 0)
        # v1 x v2 = det(
        # i j k
        # vector1
        # vector2
        # )
        # 0 + 0 + (x2-x1)(y3-y1)-(y2-y1)(x3-x1)

        ret = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
        return ret

    a, b, c, d = points
    first = ccw(a, b, c) * ccw(a, b, d)
    second = ccw(c, d, a) * ccw(c, d, b)
    if first == second == 0:
        # 일직선이면 4조각이 아니다.

        # # 일반적인 ccw일 때 서로 일직선
        # a, b = sorted(a, b)
        # c, d = sorted(c, d)
        # if a <= d and c <= b:
        #     return 1
        # else:
        #     return 0

        return 0
    else:
        if first < 0 and second < 0:
            # <=이 아닌 이유는
            # 접하는 경우는 피자가 4조각으로 잘리지 않기 때문이다.
            return 1
        else:
            return 0


temp = list(map(int, input().split()))
points = [
    (temp[0], temp[1]),
    (temp[2], temp[3]),
    (temp[4], temp[5]),
    (temp[6], temp[7]),
]


ans = sol(points)


print(ans)
