import sys
input = sys.stdin.readline


def backtrack(temp, cnt):
    if cnt == N-1:
        global max_ans, min_ans
        max_ans = max(max_ans, temp)
        min_ans = min(min_ans, temp)
        return

    for i in range(4):
        if calcs[i] > 0:
            calcs[i] -= 1
            backtrack(calculate(temp, i, numbers[cnt+1]), cnt+1)
            calcs[i] += 1
    return


def calculate(left, operator, right):
    if operator == 0:
        return left+right
    elif operator == 1:
        return left-right
    elif operator == 2:
        return left*right
    else:
        if left >= 0:
            return left//right
        else:
            return -((-left)//right)


N = int(input())
numbers = list(map(int, input().split()))
calcs = list(map(int, input().split()))
# calcs = [i for i, v in enumerate(calcs) for _ in range(v)]


max_ans = -float('inf')
min_ans = float('inf')


backtrack(numbers[0], 0)


print(max_ans)
print(min_ans)
