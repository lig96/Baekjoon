from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
dasom = int(input())
votes = [-int(input()) for _ in range(N-1)] + [-(-float('inf'))]


heapify(votes)


cnt = 0
while dasom <= -votes[0]:
    temp = heappop(votes)
    temp = (-1 * temp) - 1
    heappush(votes, -temp)

    cnt += 1
    dasom += 1


print(cnt)
