import sys
input = sys.stdin.readline


def get_dp(i):
    if i in dp:
        return dp[i]

    left = get_dp(i//P)
    right = get_dp(i//Q)
    dp[i] = left+right
    return dp[i]


N, P, Q = map(int, input().split())


dp = {}
dp[0] = 1


print(get_dp(N))
