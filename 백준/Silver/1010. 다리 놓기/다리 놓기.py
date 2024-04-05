# 방법 1: dp
# dp[n][m] = sum(dp[n-1][m-i] for i in range(1, m+1))
# 왼쪽 사이트 n개, 오른쪽 사이트 m개일 때의 정답은
# 왼쪽 사이트 맨 위를 오른쪽 (맨위, 2번째, 3번째, ~~~) 사이트에
# 연결시킨다면 오른쪽 사이트는 m-i개 남은 것과 동일하고
# 그때의 정답들의 합
#
# 방법 2: dp
# dp[n][m] = dp[n-1][m-1] + dp[n][m-1]
# 이때 dp[n][m-1]은 sum(dp[n-1][m-i] for i in range(2, m+1))과 동일
#
# 방법 3: 조합론
# mCn
# 오른쪽 사이트 m개 중 왼쪽 사이트 n개와 연결될 것을 고르는 문제
# 뽑기만 하면 순서는 자동으로 결정되니 조합을 쓴다.


import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    # 왼쪽 사이트 n개, 오른쪽 사이트 m개일 때의 정답
    dp[1] = [i for i in range(M+1)]
    for n in range(2, N+1):
        for m in range(1, M+1):
            dp[n][m] = sum(dp[n-1][m-i] for i in range(1, m+1))

    ans = dp[N][M]

    print(ans)
