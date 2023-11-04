
from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijk(graph, start):
    parent = [-1 for _ in range(n+1)]
    dist = [int(1e9) for _ in range(n+1)]
    dist[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        now_c, now_i = heappop(heap)
        if now_c > dist[now_i]:
            continue
        for next_i, next_c in graph[now_i]:
            temp = dist[now_i] + next_c
            if temp < dist[next_i]:
                dist[next_i] = temp
                heappush(heap, (temp, next_i))
                parent[next_i] = now_i
    return dist[end], parent


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, c = map(int, input().split())
    graph[start].append((end, c))
start, end = list(map(int, input().split()))


ans0, parent_arr = dijk(graph, start)
# parent_arr[i] = s에서 i까지 최단 거리로 갈 때 직전에 들른 도시.
# 1-4-5라면 parent_arr[5] = 4


print(ans0)
path = []
ans = end
while ans != -1:
    path.append(ans)
    ans = parent_arr[ans]
print(len(path))
print(*path[::-1])
