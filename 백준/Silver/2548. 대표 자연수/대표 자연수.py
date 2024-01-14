# 방법 1
# N^2 브루트 포스

# 방법 2
# MAE를 최소화하는 대푯값은 중앙값


import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))


arr.sort()


ind = (N-1)//2
ans = arr[ind]


print(ans)
