from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
cards_generator = (i for i in range(1, N+1))


dq = deque(cards_generator)
# left: 위, right: 아래


while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())


print(dq[0])
