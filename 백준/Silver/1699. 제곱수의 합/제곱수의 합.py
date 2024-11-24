import sys
input = sys.stdin.readline


N = int(input())


dp = [None for _ in range(N+1)]
dp[0] = 0


for i in range(1, N+1):
    dp[i] = min(1+dp[i-j**2] for j in range(1, int(i**0.5)+1))


print(dp[N])
