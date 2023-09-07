# pypy로 제출
from collections import deque
import sys
input = sys.stdin.readline


def calc(n, c):
    if c == 0:
        n = (2*n) % 10_000
        return n, 'D'
    elif c == 1:
        n = (n-1) % 10_000
        return n, 'S'
    elif c == 2:
        n = (n % 1_000)*10 + (n//1_000)
        return n, 'L'
    elif c == 3:
        n = (n//10) + (n % 10)*1_000
        return n, 'R'


T = int(input())
for _ in range(T):
    A, B = list(map(int, input().split()))
    visited = [False for _ in range(10_000)]

    qu = deque([(A, '')])
    visited[A] = True

    while qu:
        start, methods = qu.popleft()

        for i in range(4):
            after, now_method = calc(start, i)
            if after == B:
                print(methods+now_method)
                qu = False
                # for 문이 아니라 while 문을 break하기 위해서
                break
            if not visited[after]:
                visited[after] = True
                qu.append((after, methods+now_method))