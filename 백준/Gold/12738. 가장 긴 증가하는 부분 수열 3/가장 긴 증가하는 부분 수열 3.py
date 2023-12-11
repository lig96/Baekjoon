from bisect import bisect_left
import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))


ans = []
ans.append(-float('inf'))
# 혹은 arr[0]을 더하고 반복문을 range(1, N)으로
for v in arr:
    if ans[-1] < v:
        ans.append(v)
    else:
        ind = bisect_left(ans, v)
        ans[ind] = v


print(len(ans)-1)
