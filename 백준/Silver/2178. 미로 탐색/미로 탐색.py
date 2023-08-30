from collections import deque

N, M = map(int, input().split())
mat = []
for _ in range(N):
    temp = list(map(int, list(input())))
    mat.append(temp)


def bfs():
    visited = [[False for _ in range(M)] for _ in range(N)]
    row, col = 0, 0
    qu = deque()
    qu.append((row, col, 0))
    visited[row][col] = True
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    while qu:
        nowr, nowc, level = qu.popleft()
        if (nowr, nowc) == (N-1, M-1):
            print(level+1)
            break
        for i in range(4):
            newr, newc = nowr+dr[i], nowc+dc[i]
            if (0 <= newr <= N-1):
                if (0 <= newc <= M-1):
                    if mat[newr][newc] == 1:
                        if (not visited[newr][newc]):
                            qu.append((newr, newc, level+1))
                            visited[newr][newc] = True
    return


bfs()
