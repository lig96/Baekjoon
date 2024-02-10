from collections import deque
import sys
input = sys.stdin.readline


def bfs(startr, startc):
    qu = deque()
    qu.append((startr, startc))
    visited[startr][startc] = 0

    while qu:
        r, c = qu.popleft()
        if (ans := visited[targetr][targetc]) != -1:
            return ans

        for i in range(8):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < L and 0 <= newc < L):
                continue
            if visited[newr][newc] != -1:
                continue
            qu.append((newr, newc))
            visited[newr][newc] = visited[r][c]+1
    return


for _ in range(T := int(input())):
    L = int(input())
    startr, startc = map(int, input().split())
    targetr, targetc = map(int, input().split())

    dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    dc = [-2, -1, 1, 2, -2, -1, 1, 2]
    # 01.23
    # 45.67
    visited = [[-1 for _ in range(L)] for _ in range(L)]

    ans = bfs(startr, startc)

    print(ans)
