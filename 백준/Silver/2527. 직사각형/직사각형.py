import sys


def sol(line):
    ret = []

    point_a, point_b = line[:4], line[4:]
    a_x1, a_y1, a_x2, a_y2 = point_a
    b_x1, b_y1, b_x2, b_y2 = point_b

    if (b_x1 < a_x2 and b_x2 > a_x1) and (b_y1 < a_y2 and b_y2 > a_y1):
        ret.append('a')

    if (((b_x1 == a_x2 or b_x2 == a_x1) and (b_y1 <= a_y2 and b_y2 >= a_y1))
                ^
                (((b_x1 <= a_x2 and b_x2 >= a_x1) and (b_y1 == a_y2 or b_y2 == a_y1)))
            ):
        # x좌표가 선분에 닿는 것과 함께 y좌표가 겹치는지 확인해야 하고, vice versa임.
        # y좌표의 겹침을 확인하지 않으면 아예 겹치지 않더라도 이 경우에 해당하게 됨.
        # 선분에 닿는 걸 확인해야 하니 'a' 조건과 달리 등호가 붙어야 함.
        # or 아니고 xor해야 함.
        ret.append('b')

    if (((b_x1 == a_x2 or b_x2 == a_x1) and (True))
                and
                (((True) and (b_y1 == a_y2 or b_y2 == a_y1)))
            ):
        # if (b_x1 == a_x2 or b_x2 == a_x1) and (b_y1 == a_y2 or b_y2 == a_y1):
        ret.append('c')

    if (b_x1 > a_x2 or b_x2 < a_x1) or (b_y1 > a_y2 or b_y2 < a_y1):
        ret.append('d')

    return ret


for _ in range(4):
    line = list(map(int, sys.stdin.readline().split()))

    ans = sol(line)

    if len(ans) != 1:
        raise Exception
    sys.stdout.write(str(ans[0])+'\n')
