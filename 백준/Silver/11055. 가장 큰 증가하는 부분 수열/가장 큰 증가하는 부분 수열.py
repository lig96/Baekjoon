import sys
input = sys.stdin.readline


N = int(input())
numbers = list(map(int, input().split()))


dp = [-1 for _ in range(N)]
# dp[i] = 수열을 i번째 인덱스까지 사용했을 때의
# 증가하는 부분 수열의 합의 최댓값


for end in range(0, N):
    dp[end] = numbers[end]  # 자기 자신만을 사용
    for start in range(0, end):
        if numbers[start] < numbers[end]:
            dp[end] = max(dp[end],
                          dp[start]+numbers[end])


print(max(dp))
