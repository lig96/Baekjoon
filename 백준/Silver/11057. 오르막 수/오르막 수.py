N = int(input())


dp = [1 for _ in range(10)]
# dp[i] = 현재 자리수에 대해 맨 왼쪽 수가 i일 때 오르막 수의 개수
# 이번 경우는 오름차순이기 때문에 dp_old, dp_new 2개 필요없음
MOD = 10_007


# length가 0일 수는 없음
# length가 1이면 반복문을 안 들어가고 [1]*10 출력
for length in range(2, N+1):
    for i in range(10):
        dp[i] = sum(dp[j] for j in range(i, 10)) % MOD


print(sum(dp) % MOD)
