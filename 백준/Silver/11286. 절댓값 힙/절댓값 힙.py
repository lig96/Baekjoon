
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
print = sys.stdout.write


plus = []
minus = []


N = int(input())
for _ in range(N):
    x = int(input())
    if x != 0:
        if x > 0:
            heappush(plus, x)
        else:
            heappush(minus, -x)
    else:
        if plus and minus:
            num_plus = heappop(plus)
            num_minus = -heappop(minus)
            if abs(num_plus) < abs(num_minus):
                print(str(num_plus)+'\n')
                heappush(minus, -num_minus)
            elif abs(num_plus) > abs(num_minus):
                print(str(num_minus)+'\n')
                heappush(plus, num_plus)
            elif abs(num_plus) == abs(num_minus):
                print(str(num_minus)+'\n')
                heappush(plus, num_plus)
        elif plus and (not minus):
            num_plus = heappop(plus)
            print(str(num_plus)+'\n')
        elif (not plus) and minus:
            num_minus = -heappop(minus)
            print(str(num_minus)+'\n')
        else:
            print(str(0)+'\n')
