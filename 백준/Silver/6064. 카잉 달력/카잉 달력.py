import sys
input = sys.stdin.readline
print = sys.stdout.write


def calc(M, N, x, y):
    cnt = 0
    cnt += x
    while cnt <= M*N+1:
        temp = N if (cnt % N) == 0 else (cnt % N)
        if (temp == y):
            return cnt
        else:
            cnt += M
    else:
        return (-1)


for _ in range(T := int(input())):
    M, N, x, y = map(int, input().split())
    ans = calc(M, N, x, y)
    print(str(ans))
    print('\n')
