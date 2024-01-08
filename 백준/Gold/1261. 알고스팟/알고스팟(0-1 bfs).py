from collections import deque
import sys
input = sys.stdin.readline


def bfs(startr, startc):
    visited[startr][startc] = 0
    qu = deque([(startr, startc)])

    while qu:
        r, c = qu.popleft()
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < R and 0 <= newc < C):
                continue
            if visited[newr][newc] != -1:
                continue

            if graph[newr][newc] == 1:
                visited[newr][newc] = visited[r][c]+1
                qu.append((newr, newc))
            else:
                visited[newr][newc] = visited[r][c]
                qu.appendleft((newr, newc))
    return


C, R = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(R)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[-1 for _ in range(C)] for _ in range(R)]


bfs(0, 0)


print(visited[R-1][C-1])
