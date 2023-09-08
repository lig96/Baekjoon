from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
mat = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    mat[start].append((end, cost))

ans_start, ans_end = map(int, input().split())


def dijk(start):
    heap = []
    dist[start] = 0
    heappush(heap, (0, start))

    while heap:
        nowcost, now = heappop(heap)
        if dist[now] < nowcost:
            continue
        for end, endcost in mat[now]:
            if nowcost+endcost < dist[end]:
                dist[end] = dist[now]+endcost
                heappush(heap, (dist[end], end))


dist = [int(1e9) for _ in range(N+1)]
dijk(ans_start)
print(dist[ans_end])