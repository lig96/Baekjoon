def sol(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)

    a, b = ccw(p1, p2, p3), ccw(p1, p2, p4)
    c, d = ccw(p3, p4, p1), ccw(p3, p4, p2)
    if a == b == c == d == 0:
        # 일직선
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2):
            if min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
                # 겹치면서 일직선
                return 1
        # 안 겹치면서 일직선
        return 0
    elif a*b <= 0 and c*d <= 0:
        # 교차
        return 1
    else:
        return 0


def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # x1, y1

    left = x1*y2 + x2*y3 + x3*y1
    right = y1*x2 + y2*x3 + y3*x1
    if left > right:
        # counterclockwise
        return 1
    elif left < right:
        return -1
    elif left == right:
        return 0


line1 = map(int, input().split())
line2 = map(int, input().split())


print(sol(line1, line2))
