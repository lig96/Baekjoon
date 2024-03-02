import sys
input = sys.stdin.readline
# print = sys.stdout.write


def sol():
    ans = 0
    nowd, nows, nowe = -1, -1, -1

    for d, s, e in matches:
        if nowd < d:
            nowd, nows, nowe = d, s, e
            ans += 1
            continue

        # nowd == d:
        if nowe <= s:
            nowd, nows, nowe = d, s, e
            ans += 1
    return ans


n = int(input())
for testcase in range(n):
    m = int(input())
    matches = [list(map(int, input().split())) for _ in range(m)]

    matches.sort(key=lambda x: (x[0], x[2], x[1]))
    ans = sol()

    print(f'Scenario #{testcase+1}:')
    print(ans)
    print()
