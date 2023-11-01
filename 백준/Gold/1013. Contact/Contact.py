# 반복 사용할 땐 p = re.compile()
# search - ~
# match - 시작~
# fullmatch - 시작~끝
# ^, $를 통해 동일 작동 가능.


import re
import sys
input = sys.stdin.readline


pattern = re.compile('(100+1+|01)+')


T = int(input())
for _ in range(T):
    s = input().rstrip()

    arr = pattern.fullmatch(s)

    print('YES' if arr else 'NO')
