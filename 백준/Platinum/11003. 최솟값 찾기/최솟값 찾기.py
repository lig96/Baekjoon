# 전역 변수 실험

from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol():
    ans = []

    qu = deque()
    for i, A in enumerate(A_arr):
        # 강단조증가
        while qu and qu[-1][0] >= A:
            qu.pop()
        else:
            qu.append((A, i))

        # 조건 확인
        while qu and not (i-L+1 <= qu[0][1]):
            qu.popleft()

        ans.append(qu[0][0])
    return ans


N, L = map(int, input().split())
A_arr = list(map(int, input().split()))


ans = sol()


print(' '.join(map(str, ans)))
