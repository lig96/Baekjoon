import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
arr = list(map(int, input().split()))


ans = [-1 for _ in range(N)]
stack = []
for i, v in enumerate(arr):
    while stack and v > stack[-1][1]:
        pop_i, _ = stack.pop()
        ans[pop_i] = v
    stack.append((i, v))


for i in ans:
    print(str(i)+' ')
