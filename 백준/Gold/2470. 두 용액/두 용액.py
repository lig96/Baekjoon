import sys
input = sys.stdin.readline


N = int(input())
nums = list(map(int, input().split()))


nums.sort()


# if 0 <= nums[0]:
#     print(nums[0], nums[1])
#     exit()
# elif nums[-1] <= 0:
#     print(nums[-2], nums[-1])
#     exit()


ans = [float('inf'), (None, None)]
l, r = 0, N-1
while l < r:
    summ = nums[l]+nums[r]
    temp = [abs(summ), (nums[l], nums[r])]
    ans = min(ans, temp)
    if summ < 0:
        l += 1
    elif summ == 0:
        l += 1
    elif summ > 0:
        r -= 1


print(*ans[1])
