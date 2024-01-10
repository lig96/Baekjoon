N = int(input())


INF = float('inf')
dp = [None for _ in range(N+6)]
dp[0] = INF
dp[1] = INF
dp[2] = INF
dp[3] = 1
dp[4] = INF
dp[5] = 1


for i in range(6, N+1):
    dp[i] = min(dp[i-3], dp[i-5])+1


print(dp[N] if dp[N] != INF else -1)
