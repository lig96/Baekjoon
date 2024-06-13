import sys
input = sys.stdin.readline


def check(start):
    startr, startc = start

    available_r = (N-1) - startr
    available_c = (M-1) - startc

    if available_r >= 2:
        ret = available_c//1
    elif available_r == 1:
        ret = available_c//2
    elif available_r == 0:
        ret = 0
    else:
        raise Exception
    return ret


N, M = map(int, input().split())


during_4_moves = (2, 6)
# 4칸 이상으로 이동하려면 모두 한 번씩 사용해야 한다.
# 이때 필요한 최소 크기
after_4_moves = (0, 6)
# 모두 한 번씩 사용한 이후 도착한 지점
if during_4_moves[0] < N and during_4_moves[1] < M:
    ans = 4 + check(after_4_moves)
else:
    ans = min(3, check((0, 0)))
    # 이동 횟수가 0, 1, 2, 3


print(ans+1)
# 이동 횟수 + 1 = 방문한 칸
