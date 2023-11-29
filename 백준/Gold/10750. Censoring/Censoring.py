import sys
input = sys.stdin.readline


S = input().rstrip()
T = list(input().rstrip())


len_T, last_T = len(T), T[-1]
stack = []


for char in S:
    stack.append(char)
    if char == last_T and stack[-len_T:] == T:
        del stack[-len_T:]


print(''.join(stack))
