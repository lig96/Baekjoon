# 방법 1.
# 신발끈 공식을 이용하여 면적 구하기
#
# 방법 2.
# 큰 직사각형에서 작은 직사각형 빼기
# 이때 작은 직사각형의 가로와 세로를 구해야 한다.
# https://itcrowd2016.tistory.com/84
# 긴 가로 변의 직전과 직후에는 언제나 세로 변이 있다
# 이때 그 직전과 직후의 세로 변의 차이가
# 작은 직사각형의 세로 변의 길이이다
#
# 혹은 순회를 반시계가 아니라 시계방향으로 순회한다면
# 그 부분은 온전한 직사각형이 아니고 일부를 짜른
# 작은 영역을 지나고 있다는 뜻이다
# https://itcrowd2016.tistory.com/84


import sys
input = sys.stdin.readline


def calc_area():
    temp_a = sum(dots[i][0] * dots[i+1][1] for i in range(6))
    temp_b = sum(dots[i][1] * dots[i+1][0] for i in range(6))
    # 반시계 방향으로 회전했으니 언제나 양수
    return (temp_a-temp_b)//2


K = int(input())
arr_dir_length = [map(int, input().split()) for _ in range(6)]


dx, dy = [None, 1, -1, 0, 0], [None, 0, 0, -1, 1]
# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
dots = []
dots.append((0, 0))
for d, l in arr_dir_length:
    x, y = dots[-1]
    newx, newy = x+dx[d]*l, y+dy[d]*l
    dots.append((newx, newy))
# dots[0]과 dots[-1]은 중복되지만
# 신발끈 공식 쓸 때 필요하니 내버려둠


area = calc_area()


print(area*K)
