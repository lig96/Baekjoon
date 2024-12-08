import sys
input = sys.stdin.readline


K = int(input())
numbers = [int(input()) for _ in range(K)]


ans = []
for num in numbers:
    if num == 0:
        ans.pop()
    else:
        ans.append(num)


print(sum(ans))
