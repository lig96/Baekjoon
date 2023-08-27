import sys
from collections import deque
print = sys.stdout.write
input = sys.stdin.readline


def bfs(graph, start, visit, qu):
    for i in graph:
        qu.append((i, start))

    while qu:
        now, newstart = qu.popleft()
        if not visit[now]:
            visit[now] = True
            ans[now] = newstart
            for i in arr[now]:
                qu.append((i, now))


N = int(input())
arr = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


ans = [0 for i in range(N+1)]
visit = [False for _ in range(N+1)]
bfs(arr[1], 1, visit, deque())

print('\n'.join(map(str, ans[2:])))
