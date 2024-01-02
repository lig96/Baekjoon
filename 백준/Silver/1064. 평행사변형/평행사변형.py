# 평행사변형의 마주 보는 두 변의 길이는 같기 때문에
# D의 좌표를 구하지 않더라도 둘레를 구할 수 있다.
# 점1, 점2, 점3 간의 세 변 중 평행사변형에 쓰일
# 두 변을 선택한 뒤 2를 곱해준다.
# 점이 모두 한 직선 위에 있을 때는 평행사변형을 만들 수 없다.


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
