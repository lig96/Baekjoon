# https://www.acmicpc.net/problem/2839
# #2839 설탕배달과 동일한 문제이고
# 풀이는 해당 문제 참고.


N = int(input())


INF = float('inf')
dp = [None for _ in range(N+6)]
dp[0] = INF
dp[1] = INF
dp[2] = 1
dp[3] = INF
dp[4] = 2
dp[5] = 1


for i in range(6, N+1):
    dp[i] = min(dp[i-2], dp[i-5])+1


print(dp[N] if dp[N] != INF else -1)
