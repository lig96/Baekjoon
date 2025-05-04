import sys
input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
dr, dc = [0, 1], [1, 0]


for r in range(N):
    for c in range(N):
        if dp[r][c] == 0 or board[r][c] == 0:
            continue
        for i in range(2):
            newr, newc = r+dr[i]*board[r][c], c+dc[i]*board[r][c]
            if not (0 <= newr < N and 0 <= newc < N):
                continue
            dp[newr][newc] += dp[r][c]


print(dp[-1][-1])
