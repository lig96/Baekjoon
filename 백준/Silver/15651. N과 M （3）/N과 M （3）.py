import sys
input = sys.stdin.readline
print = sys.stdout.write


def rec(depth, temp):
    if depth == M:
        print(' '.join(map(str, temp))+'\n')
        return

    for i in range(1, N+1):
        temp.append(i)
        rec(depth+1, temp)
        temp.pop()
    return


N, M = map(int, input().split())


rec(0, [])
