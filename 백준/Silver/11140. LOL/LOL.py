# 단순 구현과 정규표현식 모두 가능하다.


import re
import sys
input = sys.stdin.readline


T = int(input())
ps = ['lol', 'ol|ll|lo|l.l', 'l|o']
for _ in range(T):
    word = input().rstrip()

    for i, p in enumerate(ps):
        if re.search(p, word):
            print(i)
            break
    else:
        print(3)


# import sys
# input = sys.stdin.readline


# T = int(input())
# for _ in range(T):
#     word = input().rstrip()
#     if 'lol' in word:
#         print(0)
#     elif 'lo' in word or 'ol' in word or 'll' in word:
#         print(1)
#     else:
#         for t in 'abcdefghijklmnopqrstuvwxyz':
#             if f'l{t}l' in word:
#                 print(1)
#                 break
#         else:
#             if 'l' in word or 'o' in word:
#                 print(2)
#             else:
#                 print(3)
