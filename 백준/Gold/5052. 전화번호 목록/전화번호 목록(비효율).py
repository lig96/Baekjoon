# 시간복잡도 O(개수 * 길이^2)


import sys
input = sys.stdin.readline


def sol(numbers):
    my_set = set()
    for num in numbers:  # O(N)
        for i in range(len(num)):  # O(len)
            temp = num[:i+1] #O(len)
            if temp in my_set:
                return 'NO'
        else:
            my_set.add(num)
    return 'YES'


t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [input().rstrip() for _ in range(n)]
    numbers.sort(key=lambda x: len(x))

    ans = sol(numbers)

    print(ans)
