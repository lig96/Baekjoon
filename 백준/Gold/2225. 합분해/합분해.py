# 방법 1: DP
# 공간복잡도 O(KN)
# 시간복잡도 O(KNN)
#
# 방법 2: DP
# 공간복잡도 O(N)
# 시간복잡도 O(KN)
#
# 방법 3: 중복조합
# 합이 정확히 N인 걸 구현하기 위해서는
# (정수 x는 1이 x개 있고 바로 옆에 칸막이가 1개 있다.)
# 와 같은 방식으로 생각 후
# 1이 정확히 N개, 칸막이가 정확히 K-1개가 놓인 상황을 생각하면
# 중복조합을 쓸 수 있다.
# H(K, N)
# C(N+K-1, K-1)


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
        dp[x] = dp[x] + (dp[x-1] if (0 <= x-1) else 0)
        dp[x] %= MOD
# 방법 1의 점화식
# dp[k][x] = summation(dp[k-1][x-L])
# where 0<=L<=N
# L이라는 크기의 정수를 1개 덜 쓴 상황의 경우의 수는
# L을 쓰면 포함할 수 있게 된다.


print(dp[N])
