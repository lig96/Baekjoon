from heapq import heappush, heappop
import sys
input = sys.stdin.readline
print = sys.stdout.write


def topology_sort():
    ans = []

    heap = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            heappush(heap, i)

    while heap:
        now = heappop(heap)
        ans.append(now)
        for end in graph[now]:
            indegree[end] -= 1
            if indegree[end] == 0:
                heappush(heap, end)
    return ans


N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1
    graph[A].append(B)


for i in topology_sort():
    print(str(i)+' ')
