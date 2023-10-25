# 펌

import sys
input = sys.stdin.readline
print = sys.stdout.write


def BOJ11723():
    S = 0
    N = int(input())
    for s in sys.stdin:
        s = s.split()
        order = s[0]
        if len(s) > 1:
            x = int(s[1])

        if order == "add":
            S += 1 << x
        elif order == "remove":
            if (S >> x) % 2:
                S -= 1 << x
        elif order == "check":
            print("{}\n".format("01"[(S >> x) % 2]))
        elif order == "toggle":
            if (S >> x) % 2:
                S -= 1 << x
            else:
                S += 1 << x
        elif order == "all":
            S = (1 << 21) - 1
        elif order == "empty":
            S = 0

for _ in range(1000):
    temp = 10*2

BOJ11723()