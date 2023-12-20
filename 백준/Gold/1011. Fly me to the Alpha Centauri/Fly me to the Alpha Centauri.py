# https://newtoner.tistory.com/51


import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    x, y = map(int, input().split())

    target_dist = y - x
    now_dist = 0
    cnt = 0
    repeated = 0

    while now_dist < target_dist:
        cnt += 1
        if cnt % 2 != 0:
            repeated += 1
        now_dist += repeated
    # cnt, repeated, 이동 가능한 거리의 상한선
    # 1, 1, ~1
    # 2, 1, ~2
    # 3, 2, ~4
    # 4, 2, ~6
    # 5, 3, ~9

    print(cnt)
