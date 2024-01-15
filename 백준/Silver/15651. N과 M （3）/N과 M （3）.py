import sys
input = sys.stdin.readline
print = sys.stdout.write


def rec(depth, temp):
    if depth == M:
        ans.append(' '.join(map(str, temp)))
        return

    for i in range(1, N+1):
        temp.append(i)
        rec(depth+1, temp)
        temp.pop()
    return


N, M = map(int, input().split())


ans = []


rec(0, [])


print('\n'.join(ans))
