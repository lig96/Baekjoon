import sys
input = sys.stdin.readline


S = list(input().rstrip())
for i in range(0, len(S)-1):
    if S[i+1] == '(':
        S[i] = int(S[i])


stack = []
for v in S:
    stack.append(v)

    if v == ')':
        temp_stack = []
        _ = stack.pop()  # 방금 넣었던 ')'가 빠짐
        while stack[-1] != '(':
            # '('가 나올 때까지 문자열, 숫자를 뺌
            temp_stack.append(stack.pop())
        _ = stack.pop()  # 매칭되는 '('가 빠짐

        temp_len = 0
        for temp_v in temp_stack:
            if type(temp_v) == int:
                temp_len += temp_v
            elif type(temp_v) == str:
                temp_len += len(temp_v)
            else:
                raise Exception

        temp_K = stack.pop()
        stack.append(temp_len*temp_K)


ans = 0
for stack_v in stack:
    if type(stack_v) == int:
        ans += stack_v
    elif type(stack_v) == str:
        ans += len(stack_v)
    else:
        raise Exception
print(ans)
