from heapq import heappush, heappop
import sys
input = sys.stdin.readline
print = sys.stdout.write


heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x != 0:
        x = x+0.1 if x < 0 else x
        sign = 1 if x > 0 else -1
        heappush(heap, (abs(x), sign))
    else:
        if heap:
            a, b = heappop(heap)
            print(str(round(a)*b)+'\n')
        else:
            print(str(0)+'\n')