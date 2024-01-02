import sys
input = sys.stdin.readline


def get_dist(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2
    return ((x1-x2)**2 + (y1-y2)**2) ** (1/2)


T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)
        continue
    dist = get_dist((x1, y1), (x2, y2))
    sum_r = r1+r2
    if dist > sum_r:
        print(0)
    elif dist == sum_r:
        print(1)
    elif dist < sum_r:
        diff_r = abs(r1-r2)
        if dist > diff_r:
            print(2)
        elif dist == diff_r:
            print(1)
        elif dist < diff_r:
            print(0)
