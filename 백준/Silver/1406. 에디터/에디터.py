import sys
input = sys.stdin.readline


left = list(input().rstrip())
right = list()
M = int(input())
for _ in range(M):
    func = input().rstrip()
    if len(func) > 1:
        func, char = func.split()

    if func == 'L':
        if left:
            temp = left.pop()
            right.append(temp)
    elif func == 'D':
        if right:
            temp = right.pop()
            left.append(temp)
    elif func == 'B':
        if left:
            left.pop()
    elif func == 'P':
        left.append(char)
ans = left+right[::-1]
print(*ans, sep='')
