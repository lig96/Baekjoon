# 파이썬 walus operator는 unpack을 지원하지 않아서
# CR과 같이 단일 객체로 받아야 한다.


from collections import deque
import sys
input = sys.stdin.readline


def bfs(startr, startc, cnt):
    visited[startr][startc] = cnt
    qu = deque([(startr, startc)])

    while qu:
        r, c = qu.popleft()
        for i in range(8):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < R and 0 <= newc < C):
                continue
            if visited[newr][newc] != 0:
                continue
            if graph[newr][newc] == 0:
                continue
            visited[newr][newc] = cnt
            qu.append((newr, newc))
    return


while (CR := list(map(int, input().split()))) != [0, 0]:
    C, R = CR
    graph = [list(map(int, input().split())) for _ in range(R)]

    visited = [[0 for _ in range(C)] for _ in range(R)]
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    # 012
    # 3.4
    # 567

    cnt = 0
    for r in range(R):
        for c in range(C):
            if visited[r][c] == 0 and graph[r][c] == 1:
                cnt += 1
                bfs(r, c, cnt)

    print(cnt)
