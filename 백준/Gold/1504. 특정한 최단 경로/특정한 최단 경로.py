from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def dijk(start):
    dist_arr = [INF for _ in range(N+1)]
    dist_arr[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        now_dist, now = heappop(heap)

        if now_dist > dist_arr[now]:
            # heap 내에서 차례가 다가오기 전에 이미 dist_arr가 갱신됨
            continue

        for end, end_dist in graph[now]:
            if dist_arr[end] > dist_arr[now] + end_dist:
                dist_arr[end] = dist_arr[now] + end_dist
                heappush(heap, (dist_arr[end], end))

    return dist_arr[1], dist_arr[v1], dist_arr[v2], dist_arr[N]


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())


INF = int(1e9)


dist_1 = dijk(1)
dist_v1 = dijk(v1)
dist_v2 = dijk(v2)
ans1 = dist_1[1] + dist_v1[2] + dist_v2[3]
# 1-v1, v1-v2, v2-n
ans2 = dist_1[2] + dist_v2[1] + dist_v1[3]
# 1-v2, v2-v1, v1-n
ans = min(ans1, ans2)

print(-1) if ans >= INF else print(ans)