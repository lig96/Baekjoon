# 투포인터


import sys
input = sys.stdin.readline


def do_two_pointer(start, end):
    '''
    inclusive start, inclusive end
    '''
    global min_sum, ans

    while start < end:
        now_sum = arr[start] + arr[end]
        if now_sum == 0:
            ans = start, end
            min_sum = now_sum
            return
        elif now_sum < 0:
            if abs(now_sum) < abs(min_sum):
                ans = (start, end)
                min_sum = now_sum
            start += 1
        elif now_sum > 0:
            if abs(now_sum) < abs(min_sum):
                ans = (start, end)
                min_sum = now_sum
            end -= 1
    else:
        return


N = int(input())
arr = list(map(int, input().split()))


if 0 <= arr[0]:
    print(arr[0], arr[1])
elif arr[-1] <= 0:
    print(arr[-2], arr[-1])
else:
    min_sum, ans = int(1e9), (None, None)
    do_two_pointer(0,  N-1)
    print(arr[ans[0]], arr[ans[1]])
