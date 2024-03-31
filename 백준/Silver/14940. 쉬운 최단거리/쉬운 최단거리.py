# 똑같은데 코드만 정리


from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write


def bfs(graph, startr, startc, visited):
    qu = deque()
    qu.append((startr, startc))
    visited[startr][startc] = 0

    while qu:
        r, c = qu.popleft()
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if 0 <= newr < R and 0 <= newc < C and visited[newr][newc] == -1:
                if graph[newr][newc] == 1:
                    # 갈 수 있는 땅
                    qu.append((newr, newc))
                    visited[newr][newc] = visited[r][c]+1
    return


R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
for r in range(R):
    for c in range(C):
        if graph[r][c] == 2:
            startr, startc = r, c


visited = [[-1 for _ in range(C)] for _ in range(R)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


bfs(graph, startr, startc, visited)


# 각 지점에서 목표지점까지의 거리를 출력한다.
# 원래 갈 수 없는 땅인 위치는 0을 출력하고,
# 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.
for r in range(R):
    for c in range(C):
        if graph[r][c] == 0:
            print(str(0)+' ')
        else:
            print(str(visited[r][c])+' ')
    print('\n')
