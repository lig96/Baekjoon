from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write


def bfs(startx):
    qu = deque()
    visited[startx] = 0
    qu.append(startx)

    while qu:
        x = qu.popleft()

        for nxt in graph[x]:
            if visited[nxt] == -1:
                visited[nxt] = visited[x]+1
                qu.append(nxt)
    return


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


visited = [-1 for _ in range(N+1)]


bfs(X)


ans = [str(i) for i, v in enumerate(visited) if v == K]
if ans:
    print('\n'.join(ans))
else:
    print(str(-1))
