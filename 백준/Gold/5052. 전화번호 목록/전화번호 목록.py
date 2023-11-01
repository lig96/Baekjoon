
# 공간복잡도 O(개수 * 2*길이)


import sys
input = sys.stdin.readline


def sol(nums):
    # for small, big in zip(nums[:-1], nums[1:]):
    for i in range(len(nums)-1):
        small, big = nums[i], nums[i+1]
        # str을 오름차순 정렬했기 때문에
        # 바로 옆자리인데 len이 크다면 접두사가 동일함
        if (len(small) < len(big)) and big.startswith(small):
            return 'NO'
    return 'YES'


t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    nums.sort()

    ans = sol(nums)

    print(ans)
