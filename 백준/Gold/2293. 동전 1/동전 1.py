import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]


dp = [0 for _ in range(k+1)]
dp[0] = 1


for coin in coins:
    for tot in range(coin, k+1):
        dp[tot] = dp[tot-coin] + dp[tot]


sys.stdout.write(str(dp[-1]))
