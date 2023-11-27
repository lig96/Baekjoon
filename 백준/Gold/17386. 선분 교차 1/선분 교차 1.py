def sol(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)

    # 선분 AB 기준 C가 있는 방향과 D가 있는 방향이 달라야 함
    left = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    # 선분 CD 기준 A가 있는 방향과 B가 있는 방향이 달라야 함
    right = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if left == -1 and right == -1:
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
