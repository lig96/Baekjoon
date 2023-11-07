S = input().rstrip('=')


num = ['ZERO', 'ONE', 'TWO', 'THREE',
       'FOUR', 'FIVE', 'SIX',
       'SEVEN', 'EIGHT', 'NINE']
oper = '+-x/'


for i, v in enumerate(num):
    S = S.replace(v, str(i))
ans1 = S+'='
# ONE을 1로 바꿔준다.
# 1234+567=


oper_stack = [x for x in S if x in oper]
for v in oper:
    S = S.replace(v, '@')
S = S.split('@')
# 연산을 위해 숫자, 연산자를 분리시켜 list로 저장한다.
# ['1234', '567']

try:
    char_stack = []
    for v in S:
        char_stack.append(v)
        if len(char_stack) == 2:
            right = int(char_stack.pop())
            left = int(char_stack.pop())
            oper = oper_stack.pop(0)
            if oper == '+':
                temp = left+right
            elif oper == '-':
                temp = left-right
            elif oper == 'x':
                temp = left*right
            elif oper == '/':
                temp = left/right
                if temp >= 0:
                    temp = int(temp//1)
                else:
                    temp = int(-((-temp)//1))
            char_stack.append(str(temp))
        else:  # len == 1일 때. 3 이상인 경우는 없음
            one = int(char_stack.pop())
            char_stack.append(str(one))
            # char_stack 내의 요소가
            # 언제나 int 가능한 str임을 보장
            # 무의미한 str 혹은 잇다른 연산자를 거름
    # 두 stack을 이용해 연산을 한다.
    # char_stack = ['1801']

    temp = char_stack[0]
    for i, v in enumerate(num):
        temp = temp.replace(str(i), v)
    ans2 = temp
    # 1을 ONE으로 바꿔준다.
    # ONEEIGHTZEROONE

    print(ans1)
    print(ans2)
except:
    print('Madness!')
