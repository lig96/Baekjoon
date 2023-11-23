import bisect
import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))


dp = []
dp.append(-float('INF'))


for item in arr:
    if item > dp[-1]:
        dp.append(item)
    else:
        i = bisect.bisect_left(dp, item)
        dp[i] = item


print(len(dp)-1)
