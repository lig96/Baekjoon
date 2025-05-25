import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))


dp = [1 for _ in range(N)]


for r in range(1, N):
    for l in range(0, r):
        if arr[r] < arr[l]:
            dp[r] = max(dp[r],
                        dp[l]+1)


print(max(dp))
