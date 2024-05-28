from collections import deque
import sys
# input = sys.stdin.readline
# print = sys.stdout.write


N, K = map(int, input().split())


qu = deque(str(i) for i in range(1, N+1))


temp = []
for _ in range(N):
    qu.rotate(-((K-1) % N))
    temp.append(qu.popleft())


print('<' + ', '.join(temp) + '>')
