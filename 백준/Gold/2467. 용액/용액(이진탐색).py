# 이진탐색


import sys
input = sys.stdin.readline


def do_bisect(start, end):
    '''
    inclusive start, inclusive end
    '''
    global ans, min_sum

    if start > end:  # 탈출문
        return

    middle = (start+end)//2
    now_sum = v+arr[middle]
    if now_sum < 0:
        if abs(now_sum) < abs(min_sum):
            ans = (i, middle)
            min_sum = now_sum
        do_bisect(middle+1, end)
    elif now_sum > 0:
        if abs(now_sum) < abs(min_sum):
            ans = (i, middle)
            min_sum = now_sum
        do_bisect(start, middle-1)
    elif now_sum == 0:
        ans = (i, middle)
        min_sum = 0
        return


N = int(input())
arr = list(map(int, input().split()))


if 0 <= arr[0]:
    print(arr[0], arr[1])
elif arr[-1] <= 0:
    print(arr[-2], arr[-1])
else:
    min_sum, ans = int(1e9), (None, None)
    for i, v in enumerate(arr):
        start, end = i+1, N-1
        do_bisect(start, end)

    print(arr[ans[0]], arr[ans[1]])
