# 위상정렬이 불가능하다면, 즉 사이클이 있다면
# 서로가 서로의 indegree를 유지시키기 때문에
# qu 내에 들어가지 못한다.


from collections import deque
import sys
input = sys.stdin.readline


def topology_sort():
    # bfs, indegree

    ans = []
    qu = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            qu.append(i)
            ans.append(i)

    while qu:
        now = qu.popleft()
        for end in graph[now]:
            indegree[end] -= 1
            if indegree[end] == 0:
                qu.append(end)
                ans.append(end)
    return ans


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    len_temp, *temp = list(map(int, input().split()))
    for s in range(0, len_temp-1):
        s, e = temp[s], temp[s+1]
        graph[s].append(e)
        indegree[e] += 1


ans = topology_sort()
if len(ans) == N:
    print(*ans, sep='\n')
else:
    print(0)
