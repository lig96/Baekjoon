from heapq import heappush, heappop
import sys
input = sys.stdin.readline
print = sys.stdout.write


def reversed_dijk(start):
    # 거꾸로기 때문에 start가 사실상 end
    dist = [float('inf') for _ in range(N+1)]
    dist[start] = 0
    heap = []
    heappush(heap, (0, start))
    # length가 앞에 와야 함

    while heap:
        now_dist, now = heappop(heap)
        if dist[now] < now_dist:
            continue

        for end, end_dist in tunnels[now]:
            temp = now_dist + end_dist
            if dist[end] > temp:
                dist[end] = temp
                heappush(heap, (temp, end))
    return dist


N, M, K = map(int, input().split())
fires = list(map(int, input().split()))
tunnels = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, length = map(int, input().split())
    tunnels[start].append((end, length))
    tunnels[end].append((start, length))
S, F = map(int, input().split())


dist = reversed_dijk(F)
# 1, ~~~, N에서 F로 가는거리


for fire in fires:
    if dist[S] >= dist[fire]:
        print(str(-1))
        break
else:
    print(str(dist[S]))
