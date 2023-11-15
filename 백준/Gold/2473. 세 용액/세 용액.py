def two_pointer(first, left, right):
    while left < right:
        now_sum = arr[first] + arr[left] + arr[right]
        update(first, left, right, now_sum)
        if now_sum > 0:
            right -= 1
        elif now_sum == 0:
            return True
        elif now_sum < 0:
            left += 1
    return False


def update(first, left, right, now_sum):
    global ans, ans_sum

    if abs(now_sum) < ans_sum:
        ans_sum = abs(now_sum)
        ans = (arr[first], arr[left], arr[right])


N = int(input())
arr = sorted(list(map(int, input().split())))


if arr[0] >= 0:
    print(*arr[:3])
elif arr[-1] <= 0:
    print(*arr[-3:])
else:
    ans, ans_sum = tuple(), float('INF')
    for first in range(0, N-2):
        if two_pointer(first, first+1, N-1):
            break
    print(*ans)
