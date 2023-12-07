from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline


def sol(heap):
    ans = 0

    heapify(heap)
    while len(heap) >= 2:
        a = heappop(heap)
        b = heappop(heap)
        ans += a+b
        heappush(heap, a+b)
    return ans


N = int(input())
arr = [int(input()) for _ in range(N)]


print(sol(arr))
