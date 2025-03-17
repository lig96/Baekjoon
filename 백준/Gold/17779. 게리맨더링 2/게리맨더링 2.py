# 1.
# 매번 선언하는 temp 위에 정직하게 경계선을 그리고 선거구를 지정한다.
# 2.
# 별도의 temp나 대입 없이 입력값 위에서 바로 인구수를 계산한다.
# 잘 관찰해보면 다음을 알 수 있다.
# 1번과 3번의 인구수의 합은 sum(board[r][:c] for r in range(s, e))이다.
# (마찬가지로 4번과 5번의 경우는 board[r][c:]이다.)
# s와 e는 경계선의 점의 좌표, 0, N이다.
# c는 r이 반복문을 돌 때마다 경계선의 점의 좌표에서부터 1씩 증가하다가
# 경계선의 점의 좌표에서 증가를 멈추게 된다.
# 5번의 합은 sum(board)-sum(1234)이다.
#
# 복잡한 구현 문제의 경우 원인덱싱, 제로인덱싱을 그대로 따르는 것이 편하다.


import sys
input = sys.stdin.readline


def color(r, c, zone):
    temp[r][c] = zone
    population[zone] += board[r][c]
    return


def draw(startx, starty, endx, endy):
    interval = abs(endx-startx)
    # assert abs(endx-startx) == abs(endy-starty)

    y_inc = bool(endy-starty >= 0)
    sign = 2*y_inc-1
    # 증가한다면 i*1, 감소한다면 i*-1로 바꿔줌

    for i in range(0, interval+1):
        if temp[startx+i][starty+(i*sign)] is None:
            # 첫 점과 끝 점이 두 번 칠해지기 때문에 중복 확인해야 함
            # 그렇다고 end=interval로 하면 안 되는 게
            # 01(2), 23(4)가 아니라 01(2), 43(2) 같은 경우가 있기 때문
            # 경우의 수 나누는 것보다는 중복 확인이 편함
            color(startx+i, starty+(i*sign), 5)
    return


def fill(zone):
    r_param = [None,
               (1, x+d1, 1),
               (1, x+d2+1, 1),
               (x+d1, N+1, 1),
               (x+d2+1, N+1, 1)][zone]
    c_param = [None,
               (1, y+1, 1),
               (N, y, -1),  # -1이라 시작, 끝이 바뀜
               (1, y-d1+d2, 1),
               (N, y-d1+d2-1, -1)][zone]  # -1이라 시작, 끝이 바뀜

    for r in range(*r_param):
        for c in range(*c_param):
            if temp[r][c] == 5:
                break
            # assert temp[r][c] is None
            color(r, c, zone)
    return


def fill_5(zone):
    for r, c in ((r, c) for r in range(1, N+1) for c in range(1, N+1)):
        if temp[r][c] is None:
            color(r, c, zone)
    return


N = int(input())
board = []
board.append([None for _ in range(N+1)])
for _ in range(N):
    temp = [None] + list(map(int, input().split()))
    board.append(temp)
# 원 인덱싱


ans = float('inf')


for x, y in ((x, y) for x in range(1, N+1) for y in range(1, N+1)):
    for d1, d2 in ((d1, d2) for d1 in range(1, N) for d2 in range(1, N)):
        if not ((1 <= x < x+d1+d2 <= N) and (1 <= y-d1 < y < y+d2 <= N)):
            continue
        temp = [[None for _ in range(N+1)] for _ in range(N+1)]
        # 원 인덱싱
        population = [None, 0, 0, 0, 0, 0]

        draw(x, y, x+d1, y-d1)
        draw(x, y, x+d2, y+d2)
        draw(x+d1, y-d1, x+d1+d2, y-d1+d2)
        draw(x+d2, y+d2, x+d2+d1, y+d2-d1)

        fill(1)
        fill(2)
        fill(3)
        fill(4)
        fill_5(5)

        ans = min(ans,
                  max(population[1:]) - min(population[1:])
                  )


print(ans)
