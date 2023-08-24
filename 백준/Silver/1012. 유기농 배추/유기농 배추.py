def bfs(graph, startx, starty, visit):
    global ans

    qu = deque()
    if not visit[startx][starty]:
        qu.append((startx, starty))
        visit[startx][starty] = True
        ans += 1
    while qu:
        nowx, nowy = qu.popleft()

        for i in range(4):
            newx, newy = nowx+dx[i], nowy+dy[i]
            if newx<0 or newy<0 or newx>=xlen or newy>=ylen:
                continue
            if graph[newx][newy] and not visit[newx][newy]:
                qu.append((newx,newy))
                visit[newx][newy] = True


import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

t = int(input())
for _ in range(t):
    xlen, ylen, k = list(map(int, input().split()))
    graph = [[False for _ in range(ylen)] for _ in range(xlen)]
    already = []
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = True
        already.append((x,y))

    visit = [[False for _ in range(ylen)] for _ in range(xlen)]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    ans = 0
    for nowx, nowy in already:
        bfs(graph, nowx, nowy, visit)
    print(str(ans)+'\n')