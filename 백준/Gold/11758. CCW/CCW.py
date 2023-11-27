# CCW
# 두 점을 지나는 직선의 방정식
# 신발끈


def sol(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # x1, y1 추가

    # 두 점을 지나는 직선의 방정식
    # left = (y3-y1)*(x2-x1)
    # right = (y2-y1)*(x3-x1)
    # 신발끈 공식
    left = (x1*y2)+(x2*y3)+(x3*y1)
    right = (y1*x2)+(y2*x3)+(y3*x1)

    if left == right:
        return 0
    elif left > right:
        return 1
    elif left < right:
        return -1


p1 = map(int, input().split())
p2 = map(int, input().split())
p3 = map(int, input().split())


print(sol(p1, p2, p3))
