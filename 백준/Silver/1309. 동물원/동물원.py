import sys
input = sys.stdin.readline


N = int(input())
MOD = 9901


dp = [1, 1, 1]  # 1번째 행일 때의 초기값
# n번째 행의 0열에 사자가 있는 상태에서 경우의 수,
# 1열에 사자가 있는 상태에서 경우의 수,
# 둘 다 없는 상태에서 경우의 수.
# 둘 다 있는 상태는 불가능함.


for _ in range(N-1):
    dp = [(dp[1]+dp[2]) % MOD,
          (dp[0]+dp[2]) % MOD,
          (dp[0]+dp[1]+dp[2]) % MOD
          ]


print(sum(dp) % MOD)
