# 방법 1
# 공간복잡도 O(KN)
# 시간복잡도 O(KNN)
#
# 방법 2
# 공간복잡도 O(N)
# 시간복잡도 O(KN)


import sys
input = sys.stdin.readline


N, K = map(int, input().split())
MOD = 1_000_000_000


dp = [0 for _ in range(N+1)]
# dp[x] = y
# 0부터 N까지의 정수 k개를 더해서
# 그 합이 x가 나오는 경우의 수는 y이다.
# k는 순회하면서 1차원 dp를 재활용할 것임.
for k in [1]:
    for x in range(0, N+1):
        dp[x] = 1
# 초기값


for k in range(2, K+1):
    for x in range(0, N+1):
        dp[x] = dp[x] + (dp[x-1] if 0 <= x-1 else 0)
        dp[x] %= MOD
# 방법 1의 점화식
# dp[k][x] = summation(dp[k-1][x-L])
# where 0<=L<=N
# 1개 덜 쓰고 그 1개의 크기가 L일 때.
# 그러한 경우가 존재하지 않는다면 dp[k-1][x-L]==0이니
# 걱정 안 해도 됨.


print(dp[N])
