import sys


def sol(line):
    ret = []

    point_a, point_b = line[:4], line[4:]
    a_x1, a_y1, a_x2, a_y2 = point_a
    b_x1, b_y1, b_x2, b_y2 = point_b

    if (b_x1 < a_x2 and b_x2 > a_x1) and (b_y1 < a_y2 and b_y2 > a_y1):
        ret.append('a')

    if (b_x1 == a_x2 or b_x2 == a_x1) ^ (b_y1 == a_y2 or b_y2 == a_y1):
        # xor
        ret.append('b')

    if (b_x1 == a_x2 or b_x2 == a_x1) and (b_y1 == a_y2 or b_y2 == a_y1):
        ret.append('c')

    if (b_x1 > a_x2 or b_x2 < a_x1) or (b_y1 > a_y2 or b_y2 < a_y1):
        ret.append('d')

    if 'd' in ret and 'b' in ret:
        ret.remove('b')
    return ret


for line in sys.stdin.readlines():
    line = line.rstrip()
    line = list(map(int, line.split()))

    ans = sol(line)

    if len(ans) == 0:
        print(line)
        exit(2)
    if len(ans) >= 2:
        print(line, ans)
        raise RecursionError
    sys.stdout.write(str(ans[0])+'\n')
