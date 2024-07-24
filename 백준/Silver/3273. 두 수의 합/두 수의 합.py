from collections import defaultdict
import sys
input = sys.stdin.readline


N = int(input())
numbers = list(map(int, input().split()))
x = int(input())
# 1 ≤ n ≤ 100_000


numbers.sort()


ans = 0
l, r = 0, N-1
while l < r:
    if (sum_ := numbers[l]+numbers[r]) == x:
        ans += 1
        l += 1
        r -= 1
    elif sum_ < x:
        l += 1
    elif sum_ > x:
        r -= 1


print(ans)
