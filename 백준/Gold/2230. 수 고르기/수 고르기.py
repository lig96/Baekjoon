# 투포인터


import sys
input = sys.stdin.readline


def do_two_pointer(start, end):
    '''
    inclusive start, inclusive end
    '''
    global min_diff

    while start <= end < N:
        now_diff = arr[end]-arr[start]
        if now_diff == M:
            min_diff = now_diff
            return
        elif now_diff < M:
            end += 1
        elif now_diff > M:
            if now_diff < min_diff:
                min_diff = now_diff
            start += 1
    else:
        return


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]


arr.sort()
min_diff = int(2e9)


do_two_pointer(0, 0)
print(min_diff)
