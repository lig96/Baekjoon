import sys
input = sys.stdin.readline


def product(arr):
    ret = 1
    for i in arr:
        ret *= i
    return ret


R, C = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(R)]


prefixsum = [[0 for _ in range(C+1)] for _ in range(R+1)]
for r in range(1, R+1):
    for c in range(1, C+1):
        prefixsum[r][c] = (-prefixsum[r-1][c-1] +
                           prefixsum[r-1][c] +
                           prefixsum[r][c-1] +
                           board[r-1][c-1]  # 1인덱싱->0인덱싱
                           )
# [0, 0, 0, 0]
# [0, 1, 3, 6]
# [0, 5, 12, 21]
# [0, 12, 27, 45]


ans = -float('inf')
# 위아래로 길쭉한 사각형 3개
for c1 in range(0, C-2):
    for c2 in range(c1+1, C-1):
        # c1, c2, C = 1, 5, 6이라 하자.
        # t1 = 0, 1
        # t2 = 2, 3, 4, 5
        # t3 = 6
        # 이렇게 되려면 c2의 끝 범위가 C-1 미만이어야 함.
        t1 = prefixsum[R][c1+1]
        t2 = prefixsum[R][c2+1] - t1
        t3 = prefixsum[R][C] - t1 - t2
        ans = max(ans, product([t1, t2, t3]))
# 좌우로 널따란 사각형 3개
for r1 in range(0, R-2):
    for r2 in range(r1+1, R-1):
        t1 = prefixsum[r1+1][C]
        t2 = prefixsum[r2+1][C] - t1
        t3 = prefixsum[R][C] - t1 - t2
        ans = max(ans, product([t1, t2, t3]))
# 특정 점을 기준으로 4분면
for r, c in ((r, c) for r in range(R-1) for c in range(C-1)):
    # t1 t2
    # t3 t4 형태.
    t1 = prefixsum[r+1][c+1]
    t2 = prefixsum[r+1][C] - t1
    t3 = prefixsum[R][c+1] - t1
    t4 = prefixsum[R][C] - t1 - t2 - t3
    ans = max(ans, product([t1+t2, t3, t4]))
    ans = max(ans, product([t1+t3, t2, t4]))
    ans = max(ans, product([t1, t3, t2+t4]))
    ans = max(ans, product([t1, t2, t3+t4]))


print(ans)
