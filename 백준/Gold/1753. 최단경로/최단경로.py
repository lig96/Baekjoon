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

        for after, after_dist in graph[now]:
            temp = dist_arr[now] + after_dist
            if dist_arr[after] > temp:  # 라인 A
                dist_arr[after] = temp
                heappush(heap, (temp, after))


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
# 인덱싱을 1부터 하기 위해 V+1
# 중복 간선을 최소 경로로 초기화하기 위해 dict를 쓸 수 있지만
# 오히려 느리다. 라인 A에서 어차피 크기 비교가 이루어지기 때문에
# 인접 리스트를 만드는 과정에서 크기 비교를 중복할 필요가 없는 듯하다.
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


INF = int(1e9)
dist_arr = [INF for _ in range(V+1)]
heap = []


dijk(K)


for value in dist_arr[1:]:
    print(str(value) if value < INF else 'INF')
    print('\n')
