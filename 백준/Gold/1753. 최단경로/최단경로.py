
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
print = sys.stdout.write


def dijk(start):
    dist_arr[start] = 0
    heappush(heap, (0, start))

    while heap:
        now_dist, now = heappop(heap)
        if dist_arr[now] < now_dist:
            continue

        # for afters in graph[now].items():
        for afters in graph[now]:
            after, after_dist = afters

            temp_dist = dist_arr[now] + after_dist
            if dist_arr[after] > temp_dist:
                dist_arr[after] = temp_dist
                heappush(heap, (temp_dist, after))
    return dist_arr


V, E = map(int, input().split())
K = int(input())
# graph = [{} for _ in range(V+1)]
graph = [[]for _ in range(V+1)]
# 인덱싱을 1부터 하기 위해 V+1
# 여러 E를 최소 경로로 초기화하기 위해 딕셔너리
for _ in range(E):
    u, v, w = map(int, input().split())
    # try:
    #     graph[u][v] = min(graph[u][v], w)
    # except:
    #     graph[u][v] = w
    graph[u].append((v, w))


INF = int(1e9)
dist_arr = [INF for _ in range(V+1)]
heap = []


dijk(K)


for i in range(1, V+1):
    print(str(dist_arr[i]) if dist_arr[i] < INF else 'INF')
    print('\n')
