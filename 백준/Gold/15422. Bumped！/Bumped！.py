from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijk(x, adj):
    dist = [float('inf') for _ in range(n)]
    heap = []
    dist[x] = 0
    heappush(heap, (dist[x], x))

    while heap:
        dist_now, now = heappop(heap)
        if dist_now > dist[now]:
            continue
        for nxt, cost in adj[now]:
            if dist[nxt] > dist_now + cost:
                dist[nxt] = dist_now + cost
                heappush(heap, (dist[nxt], nxt))
    return dist


n, m, f, s, t = map(int, input().split())
roads = [[] for _ in range(n)]
for _ in range(m):
    i, j, c = map(int, input().split())
    roads[i].append((j, c))
    roads[j].append((i, c))
flights = [tuple(map(int, input().split())) for _ in range(f)]


dist_s2x = dijk(s, roads)
dist_x2t = dijk(t, roads)


ans = dist_s2x[t]  # 비행기 사용 안 하는 경우
for u, v in flights:
    temp = dist_s2x[u] + 0 + dist_x2t[v]
    ans = min(temp, ans)  # 비행기 1회 사용하는 경우


print(ans)
