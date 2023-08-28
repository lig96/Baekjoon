
from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


def bfs(graph, start, visit):
    qu = deque()
    qu.append((start, 0))
    visit[start] = True
    ans = 0

    while qu:
        before, level = qu.popleft()
        for friend in graph[before]:
            if not visit[friend]:
                visit[friend] = True
                qu.append((friend, level+1))
                ans += level+1
    return ans


ans_l = []
for i in range(1, N+1):
    visit = [False for _ in range(N+1)]
    ans = bfs(graph=graph, start=i, visit=visit)
    ans_l.append(ans)


print(ans_l.index(min(ans_l))+1)
