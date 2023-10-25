# S는 이진수로 표현된 집합.
# 11010은 1, 3, 4를 뜻함.
# x=3는 1<<3를 뜻함. 즉 1000, 8

import sys
input = sys.stdin.readline
print = sys.stdout.write


S = 0
M = int(input())


for _ in range(M):
    temp = input().split()
    if len(temp) == 2:
        calc, x = temp
        x = 1 << int(x)
    else:
        calc = temp[0]

    if calc == 'add':
        S = S | x
    elif calc == 'remove':
        S = S & (~x)
    elif calc == 'check':
        # if S & x:
        #     print(1)
        # else:
        #     print(0)
        print(str(int(bool(S & x)))+'\n')
    elif calc == 'toggle':
        S = S ^ x
    elif calc == 'all':
        S = (1 << 21) - 1
    elif calc == 'empty':
        S = 0
