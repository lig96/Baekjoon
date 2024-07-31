from collections import deque
import sys
input = sys.stdin.readline


def bfs(startx):
    qu = deque()
    visited[startx] = 0
    qu.append(startx)
    while qu:
        x = qu.popleft()
        for dx in [U, -D]:
            newx = x+dx
            if not (1 <= newx <= F):
                continue
            if visited[newx] >= 0:
                continue
            visited[newx] = visited[x]+1
            qu.append(newx)
    return


F, S, G, U, D = map(int, input().split())


visited = [-1 for _ in range(F+1)]
bfs(S)


print("use the stairs" if visited[G] == -1 else visited[G])
