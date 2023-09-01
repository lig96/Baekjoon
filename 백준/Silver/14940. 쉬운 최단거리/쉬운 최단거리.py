from collections import deque


n, m = map(int, input().split())
mat = []
loc = False
for row in range(n):
    temp = list(map(int, input().split()))
    mat.append(temp)

    if (not loc) and (2 in temp):
        loc = (row, temp.index(2))


visit = [['N' for _ in range(m)] for _ in range(n)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(graph, v, visit):
    row, col = v
    qu = deque()
    qu.append((row, col, 0))
    visit[row][col] = 0

    while qu:
        nowr, nowc, nowlevel = qu.popleft()

        for i in range(4):
            newr, newc = nowr+dr[i], nowc+dc[i]

            if (0 <= newr < n) and (0 <= newc < m):
                # mat 안이라면
                if (visit[newr][newc] == 'N'):
                    # visit 아닌 상태
                    if mat[newr][newc] == 1:
                        # 갈 수 있는 땅
                        visit[newr][newc] = nowlevel+1
                        qu.append((newr, newc, nowlevel+1))
                    elif mat[newr][newc] == 0:
                        # 갈 수 없는 땅
                        visit[newr][newc] = 0


bfs(mat, loc, visit)

for row in range(len(visit)):
    for col in range(len(visit[0])):
        if (visit[row][col] == 'N') and (mat[row][col] == 1):
            visit[row][col] = -1
        elif (visit[row][col] == 'N') and (mat[row][col] == 0):
            visit[row][col] = 0
for row in visit:
    print(*row)
