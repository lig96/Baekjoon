import sys
input = sys.stdin.readline


def sol(r, c, d):
    if not (0 <= r < N and 0 <= c < N):
        return 0
    if dp[r][c][d][1]:
        return dp[r][c][d][0]

    flag = False
    if d == 0:
        try:
            if board[r][c] == 1:
                flag = True
        except IndexError:
            flag = True
    elif d == 1:
        try:
            if board[r][c] == 1 or board[r-1][c] == 1 or board[r][c-1] == 1:
                flag = True
        except IndexError:
            flag = True
    elif d == 2:
        try:
            if board[r][c] == 1:
                flag = True
        except IndexError:
            flag = True
    if flag:
        dp[r][c][d] = [0, True]
        return dp[r][c][d][0]


    temp = []
    if d == 0:
        temp.append(sol(r, c-1, 0))
        temp.append(sol(r, c-1, 1))
    elif d == 1:
        temp.append(sol(r-1, c-1, 0))
        temp.append(sol(r-1, c-1, 1))
        temp.append(sol(r-1, c-1, 2))
    elif d == 2:
        temp.append(sol(r-1, c, 1))
        temp.append(sol(r-1, c, 2))
    dp[r][c][d] = [sum(temp), True]
    return dp[r][c][d][0]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# 제로 인덱싱
# 빈 칸은 0, 벽은 1
# (0, 0)과 (0, 0)는 항상 빈 칸이다.


dp = [[[[0, False] for _ in range(3)] for _ in range(N)] for _ in range(N)]
# dp[r][c][d] = 파이프의 오른쪽 아래 끝이 board[r][c]에 위치해있고
# 방향이 d일 때 그러한 도착이 가능하게 하는 [경우의 수, 방문 여부]
# d = 0, 노란색 가로
# d = 1, 파란색 대각선
# d = 2, 초록색 세로
dp[0][1][0] = [1, True]
# 초깃값


ans = 0
for d in range(3):
    ans += sol(N-1, N-1, d)


print(ans)
