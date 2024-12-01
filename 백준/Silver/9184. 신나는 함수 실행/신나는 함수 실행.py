import sys
input = sys.stdin.readline
sys_print = sys.stdout.write
# sys.setrecursionlimit(int(20**3)+100)


def sol(a, b, c):
    if (a, b, c) in dp:
        return dp[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        dp[(a, b, c)] = 1
    elif a > 20 or b > 20 or c > 20:
        dp[(a, b, c)] = sol(20, 20, 20)
    elif a < b and b < c:
        dp[(a, b, c)] = (sol(a, b, c-1) +
                         sol(a, b-1, c-1) -
                         sol(a, b-1, c))
    else:
        dp[(a, b, c)] = (sol(a-1, b, c) +
                         sol(a-1, b-1, c) +
                         sol(a-1, b, c-1) -
                         sol(a-1, b-1, c-1))
    return dp[(a, b, c)]


dp = dict()
while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break

    ans = sol(a, b, c)

    sys_print(f"w({a}, {b}, {c}) = {ans}"+"\n")
