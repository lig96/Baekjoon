import sys
input = sys.stdin.readline


def sol(K, arr):
    dp = [[-1 for _ in range(K)] for _ in range(K)]
    # inclusive K
    # dp[1][3] = arr[1] ~ arr[3]을 활용했을 때 최소 비용
    # 언제나 새 값으로 갱신되기 때문에 초기값은 상관 없음

    presum = [0 for _ in range(K+1)]
    for i in range(K):
        presum[i+1] = presum[i] + arr[i]

    for i in range(K):
        dp[i][i] = 0
    for i in range(K-1):
        dp[i][i+1] = arr[i] + arr[i+1]
    for width in range(2, K):
        for i in range(K-width):
            # for mid in range(width):
            #     temp_a = dp[i][i+mid]+dp[i+mid+1][i+width]
            #     temp_b = presum[i+width+1]-presum[i]
            #     temp = temp_a + temp_b
            #     if temp < dp[i][i+width]:
            #         dp[i][i+width] = temp
            dp[i][i+width] = min(
                dp[i][i+mid]+dp[i+mid+1][i+width] for mid in range(width)
            ) + presum[i+width+1]-presum[i]

    return dp[0][-1]


T = int(input())
for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))

    print(sol(K, arr))
