import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(N, arr):
    break_i = None
    prev = -float('inf')
    for i in reversed(range(0, N)):
        v = arr[i]
        if v > prev:
            prev = v
        else:
            break_i = i
            break

    if break_i is None:
        return str(-1)

    next_smallest_i = None
    next_smallest_v = float('inf')
    for i in range(break_i+1, N):
        v = arr[i]
        if (v < next_smallest_v) and (v > arr[break_i]):
            next_smallest_i = i
            next_smallest_v = v

    arr[break_i], arr[next_smallest_i] = (
        arr[next_smallest_i], arr[break_i]
    )

    arr[break_i+1:] = sorted(arr[break_i+1:])

    return ' '.join(map(str, arr))


N = int(input())
arr = list(map(int, input().split()))


ans = sol(N, arr)


print(ans)
