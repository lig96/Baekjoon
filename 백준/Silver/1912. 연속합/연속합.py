import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))


dp = [[None for _ in range(2)] for _ in range(N)]
# dp[n][0] = arr[0]~arr[n]의 arr[n]을 안 쓴 최대 연속합
# dp[n][1] = arr[0]~arr[n]의 arr[n]을 쓴 최대 연속합
for n in [0]:
    dp[n][0] = -float('inf')
    dp[n][1] = arr[n]


for n in range(1, N):
    dp[n][0] = max(dp[n-1])
    dp[n][1] = max(dp[n-1][1] + arr[n],  # 이전에 이어서
                   arr[n])  # 이전에 안 이어서
#
# dp[n] = arr[0]~arr[n]의 arr[n]을 쓴 최대 연속합
# dp[n] = max(dp[n-1]+arr[n], arr[n])
# print(max(dp[0:n+1]))
# 도 가능하다.


print(max(dp[n]))
