import sys
input = sys.stdin.readline


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]


INF = float('inf')
dp = [[[INF for _ in range(3)] for _ in range(C)] for _ in range(R)]
# dp[r][c][d] = min(dp[r-1][c + -1, 0, 1][not d])
# d = [0, 1, 2] = [좌, 직진, 우]
for c in range(C):
    dp[0][c] = [board[0][c] for _ in range(3)]
# 초기값
dc = [1, 0, -1]


for r in range(1, R):
    for c in range(C):
        for d in range(3):
            dp[r][c][d] = min((dp[r-1][c+dc[d]][temp]
                              for temp in range(3) if temp != d and 0 <= c+dc[d] < C),
                              default=INF) + board[r][c]


print(min(map(min, dp[-1])))
