import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)
        continue

    dist = ((x1-x2)**2 + (y1-y2)**2) ** (1/2)
    sum_r = r1+r2
    diff_r = abs(r1-r2)

    if dist == sum_r:
        # 외접
        print(1)
    elif dist > sum_r:
        # 외접보다 멂
        print(0)
    elif dist < sum_r:
        # 외접보다 가까움
        if dist == diff_r:
            # 내접
            print(1)
        elif dist > diff_r:
            # 내접보다 멂
            print(2)
        elif dist < diff_r:
            # 내접보다 가까움
            print(0)
