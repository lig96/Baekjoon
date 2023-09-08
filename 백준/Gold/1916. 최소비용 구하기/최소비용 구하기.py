from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
# 반복문
mat = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, c = map(int, input().split())
    mat[start].append((end, c))
# 리스트 축약
# mat = [[] for _ in range(N+1)]
# [mat[start].append((end, c)) for start, end, c in
#  (map(int, input().split()) for _ in range(M))]
ans_start, ans_end = map(int, input().split())


def dijk(start):
    heap = []
    dist[start] = 0
    heappush(heap, (0, start))

    while heap:
        start_now, now_i = heappop(heap)
        if dist[now_i] < start_now:
            continue
        for end_i, now_end in mat[now_i]:
            if start_now+now_end < dist[end_i]:
                dist[end_i] = start_now+now_end
                heappush(heap, (dist[end_i], end_i))


dist = [int(1e9) for _ in range(N+1)]
dijk(ans_start)
print(dist[ans_end])
