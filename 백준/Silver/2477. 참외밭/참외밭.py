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
