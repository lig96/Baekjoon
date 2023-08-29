from heapq import heappush, heappop
import sys
input = sys.stdin.readline
print = sys.stdout.write


plus = []
minus = []


N = int(input())
for _ in range(N):
    x = int(input())

    if x > 0:
        heappush(plus, x)
    elif x < 0:
        heappush(minus, -x)
    else:
        if plus and minus:
            if plus[0] < minus[0]:
                print(str(heappop(plus))+'\n')
            else:
                print(str(-heappop(minus))+'\n')
        elif plus and (not minus):
            print(str(heappop(plus))+'\n')
        elif (not plus) and minus:
            print(str(-heappop(minus))+'\n')
        else:
            print(str(0)+'\n')
