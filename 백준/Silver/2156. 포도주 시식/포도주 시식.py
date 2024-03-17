import sys
input = sys.stdin.readline


N = int(input())
cups = [int(input()) for _ in range(N)]
# 제로 인덱싱


dp = [[-1 for _ in range(3)] for _ in range(N)]
# dp[i][012] =
# i번째 인덱스 시점에서 연속된 0, 1, 2개를 사용했을 때
# 최대 포도주 섭취량


dp[0][0] = 0
dp[0][1] = cups[0]
dp[0][2] = 0
for i in range(1, N):
    dp[i][0] = 0 + max(dp[i-1])
    dp[i][1] = cups[i] + dp[i-1][0]
    dp[i][2] = cups[i] + dp[i-1][1]


print(max(dp[N-1]))
