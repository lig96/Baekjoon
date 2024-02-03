# 백준 2293, 동전 1과 유사함
# 3중 반복문 냅색 문제를 점화식을 바꿔 2중 반복문으로 변환


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]


coins = sorted(set(coins))  # 안 해도 됨
dp = [float('inf') for _ in range(k+1)]
dp[0] = 0


for coin in coins:
    for tot in range(coin, k+1):
        dp[tot] = min(dp[tot-coin]+1, dp[tot])


if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])
