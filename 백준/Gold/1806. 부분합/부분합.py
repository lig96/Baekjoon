import sys
input = sys.stdin.readline


N, S = map(int, input().split())
arr = list(map(int, input().split()))


dp, temp = [0], 0
for i in arr:
    temp = temp + i
    dp.append(temp)
# sum(arr[start:end]) == dp[end] - dp[start]
# dp[i]는 i 미만의 누적합


if S > dp[N]:  # sum(arr)
    print(0)
else:
    start, end = 0, 0
    ans = N
    while end <= N:
        temp = dp[end]-dp[start]
        if temp >= S:
            if end-start < ans:
                ans = end-start
                if ans == 1:
                    break
            start += 1
        else:
            end += 1
    print(ans)
