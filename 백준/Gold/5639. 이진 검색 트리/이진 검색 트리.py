import sys
sys.setrecursionlimit(10**5)


lines = sys.stdin.readlines()
nums = [int(line) for line in lines]


def rec(start, end):
    if start == end:
        return

    middle = end
    # 더 큰 값이 없는 경우
    for i in range(start, end):
        if nums[start] < nums[i]:
            middle = i
            break

    rec(start+1, middle)  # left
    rec(middle, end)  # right
    print(nums[start])


rec(0, len(nums))