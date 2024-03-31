# 1. 다이나믹프로그래밍
# dp[i][0혹은1] = i번째 성냥이 0 혹은 1일 때
# i번째 성냥까지 모두 불을 피우면서 필요한 최소 뒤집는 개수
#
# 2. 누적합
# min(0~i까지 모두 1로 만들기+ i~N까지 모두 0으로 만들기)
# 배열의 합으로 구할 수 있고 누적합(특히 슬라이딩 윈도우)을 쓰면 편하다.


import sys
input = sys.stdin.readline


def sol_dp(numbers, N):
    dp = [[-1 for _ in range(2)] for _ in range(N)]
    # dp[i][0|1] = i번째 성냥까지 불을 피우면서
    # i번째 성냥이 0 혹은 1일 때
    # 필요한 최소 뒤집는 개수
    if numbers[0] == 0:
        dp[0] = [0, 1]
    else:
        dp[0] = [1, 0]

    for i in range(1, N):
        if numbers[i] == 0:
            dp[i][0] = min(dp[i-1])
            dp[i][1] = dp[i-1][1] + 1
        else:
            dp[i][0] = min(dp[i-1]) + 1
            dp[i][1] = dp[i-1][1]

    return min(dp[N])


def sol_prefixsum(numbers, N):
    ret = float('inf')
    right_becomes_0 = numbers.count(1)
    left_becomes_1 = 0

    ret = min(ret, left_becomes_1+right_becomes_0)

    for i in range(N):
        if numbers[i] == 1:
            right_becomes_0 -= 1
        elif numbers[i] == 0:
            left_becomes_1 += 1

        ret = min(ret, left_becomes_1+right_becomes_0)
    return ret


N = int(input())
numbers = list(map(int, input().split()))


ans = sol_prefixsum(numbers, N)


print(ans)
