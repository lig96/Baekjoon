N = int(input())
MOD = 15746


dp = [0 for _ in range(N+2)]
dp[0] = 1
dp[1] = 1


for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD


print(dp[N])
