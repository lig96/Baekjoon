

import sys
input = sys.stdin.readline


def sol(s):
    st = 0
    states = {}
    # 다음state = states[현재state][입력]
    states[0] = [1, 2]  # default 혹은 right01이 끝난 후
    states[1] = [99, 0]  # right, 0
    states[2] = [3, 99]  # left, 1
    states[3] = [4, 99]  # left, 10
    states[4] = [4, 5]  # left, 100+
    states[5] = [1, 6]  # left, 100+1
    states[6] = [7, 6]  # left, 100+11
    states[7] = [4, 0]  # left, 100+110
    states[99] = [99, 99]

    for char in s:
        st = states[st][int(char)]
        # print(st, char)
    return st


T = int(input())
for _ in range(T):
    s = input().rstrip()

    ans = sol(s)

    if ans in [0, 5, 6]:
        print('YES')
    else:
        print('NO')
