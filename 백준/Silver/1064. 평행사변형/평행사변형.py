def find_dist(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)


x1, y1, x2, y2, x3, y3 = map(int, input().split())
dot1, dot2, dot3 = (x1, y1), (x2, y2), (x3, y3)


if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
    # 두 점을 지나는 직선의 기울기 공식 변형
    print(-1.0)
else:
    line12 = find_dist(dot1, dot2)
    line13 = find_dist(dot1, dot3)
    line23 = find_dist(dot2, dot3)
    perimeters = [
        2*(line12+line13),
        2*(line12+line23),
        2*(line13+line23)
    ]

    print(max(perimeters)-min(perimeters))
