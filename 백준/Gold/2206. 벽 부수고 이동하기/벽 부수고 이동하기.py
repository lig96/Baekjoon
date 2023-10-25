
from collections import deque
import sys
input = sys.stdin.readline


def bfs(row, col, wall):
    visited[row][col][0] = 1
    qu = deque()
    qu.append((row, col, 0))

    while qu:
        r, c, wall = qu.popleft()

        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if (0 <= newr < N) and (0 <= newc < M):
                if wall == 0:  # 벽을 뚫을 수 있는 여유가 있다면
                    if mat[newr][newc] == '0' and not visited[newr][newc][0]:
                        visited[newr][newc][0] = visited[r][c][0]+1
                        qu.append((newr, newc, wall))
                    if mat[newr][newc] == '1' and not visited[newr][newc][1]:
                        visited[newr][newc][1] = visited[r][c][0]+1
                        qu.append((newr, newc, wall+1))
                else:
                    if mat[newr][newc] == '0' and not visited[newr][newc][1]:
                        visited[newr][newc][1] = visited[r][c][1]+1
                        qu.append((newr, newc, wall))


N, M = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(N)]


visited = [[[False, False] for _ in range(M)] for _ in range(N)]
# visited[row][col][0] = 벽뚫기 안 쓴 상태로 방문
# visited[row][col][1] = 벽뚫기 쓴 상태로 방문
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]


bfs(0, 0, 0)


a, b = visited[N-1][M-1]
if a and b:
    print(min(a, b))
elif not a and not b:
    print(-1)
else:
    print(max(a, b))
    # print(max(False, 1234))
