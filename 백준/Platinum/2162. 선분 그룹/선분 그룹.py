# ccw 알고리즘에는 신발끈 공식과 외적이 있는데
# 후자가 연산이 빠르고 코드가 짧다.

# 방법 1. 신발끈 공식
# right_down = x1*y2+x2*y3+x3*y1  # \ 모양의 대각선
# left_down = y1*x2+y2*x3+y3*x1  # / 모양의 대각선
# temp = right_down - left_down
# 방법 2. 외적
# |x2-x1 y2-y1|
# |x3-x1 y3-y1|
# 위와 같은 행렬의 판별식 ad-bc
# temp = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

# 또한 line = Line(Point(x1, y1), Point(x2, y2))와 같이
# 선과 점을 클래스로 구현하면 짜임새있게 코딩할 수 있다.


from collections import Counter
import sys
input = sys.stdin.readline


def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def ccw(x1, y1, x2, y2, x3, y3):
    temp = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    if temp > 0:
        # ccw 방향
        return 1
    elif temp == 0:
        return 0
    else:
        return -1


def can_meet(left, right):
    x1, y1, x2, y2 = left
    x3, y3, x4, y4 = right

    left_3 = ccw(x1, y1, x2, y2, x3, y3)
    left_4 = ccw(x1, y1, x2, y2, x4, y4)
    right_1 = ccw(x3, y3, x4, y4, x1, y1)
    right_2 = ccw(x3, y3, x4, y4, x2, y2)

    l, r = left_3*left_4, right_1*right_2

    if l == 0 and r == 0:
        # 서로 일직선에 있음
        # (0, 0)
        if max(x1, x2) < min(x3, x4):
            return False
        if max(x3, x4) < min(x1, x2):
            return False
        if max(y1, y2) < min(y3, y4):
            return False
        if max(y3, y4) < min(y1, y2):
            return False
        return True
    else:
        if l == 1 or r == 1:
            # 명백하게 한쪽 사이드로 치우쳐짐
            # (-1, 1), (0, 1), (1, -1), (1, 0), (1, 1)
            return False
        else:  # if l == -1 or r == -1:
            # 1은 명백하게 만남. 2, 3은 T자처럼 스치듯이 만남
            # (-1, -1), (-1, 0), (0, -1)
            return True


N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]


parent = [i for i in range(N)]


for left_i in range(0, N):
    left = lines[left_i]
    for right_i in range(left_i+1, N):
        right = lines[right_i]
        if can_meet(left, right):
            union(left_i, right_i)


ans = Counter(find(i) for i in range(N))
print(len(ans))
print(ans.most_common(1)[0][1])
# 가장 큰 것 1개, 0번째로 큰 것, 키와 밸류 중 밸류
