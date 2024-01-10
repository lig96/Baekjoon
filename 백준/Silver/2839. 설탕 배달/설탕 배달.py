# 방법 1.
# 브루트 포스
# N이 작기 때문에 N = 5*x + 3*y를 성립시키는
# x와 y를 일일이 구한다.
# 그리디적인 접근 방법을 취해 x를 가장 큰 것일때부터
# 순회를 하면 조금 더 빠르다.

# 방법 2.
# dp
# 점화식 dp[i] = min(dp[i-3], dp[i-5])+1

# 방법 3.
# 수학
# https://st-lab.tistory.com/72
# # if (n == 4) or (n == 7):
# #     ans = -1
# # elif (n % 5 == 0):
# #     ans = (n // 5)
# # elif (n % 5 == 1) or (n % 5 == 3):
# #     ans = (n // 5) + 1
# # elif (n % 5 == 2) or (n % 5 == 4):
# #     ans = (n // 5) + 2
# O(1)이지만 떠올리기 어렵다.


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
