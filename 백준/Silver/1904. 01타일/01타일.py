N = int(input())
MOD = 15746


dp = [0 for _ in range(N+3)]
dp[0] = 0
dp[1] = 1
dp[2] = 2


for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD


print(dp[N])
