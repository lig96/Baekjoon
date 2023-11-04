# <stack[-1] != '('>
# 현재 있는 괄호 내에서만 해야 함
#
# <stack[-1] in '*/'>
# 먼저 입력된 게 먼저 출력되어야 하긴 함
# 하지만 자기 자신이 */라면 늦었지만 +-보다 먼저 출력되어야 함
# +-라면 출력하지 않음
# 늦은 */보다는 빠른 */이 먼저 출력해도 됨


STRING = input()

ans = ''
stack = []
for s in STRING:
    if s.isalpha():
        ans += s
    elif s in '(':
        stack.append(s)
    elif s in '*/':
        while stack and stack[-1] != '(' and stack[-1] in '*/':
            ans += stack.pop()
        stack.append(s)
    elif s in '+-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(s)
    elif s in ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
else:
    while stack:
        ans += stack.pop()

print(ans)
