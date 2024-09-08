import sys
input = sys.stdin.readline


N = int(input())
P = [None] + list(map(int, input().split()))


dp = [None for _ in range(N+1)]
dp[0] = 0
dp[1] = P[1]


for i in range(2, N+1):
    dp[i] = max(dp[i-j] + P[j] for j in range(1, i+1))


print(dp[N])
