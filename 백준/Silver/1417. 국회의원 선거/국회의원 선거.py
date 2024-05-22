from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
dasom = int(input())
votes = [int(input()) for _ in range(N-1)]


heap = []
for vote in votes:
    heappush(heap, -vote)
heappush(heap, -(-float('inf')))
# 최대힙이라서 마이너스 붙여줘야 함.
# IndexError 방지하기 위해 매우 작은 값 하나 넣어줌.


cnt = 0
while dasom <= -heap[0]:
    temp = heappop(heap)
    temp = (-1 * temp) - 1
    heappush(heap, -temp)
    cnt += 1
    dasom += 1


print(cnt)
