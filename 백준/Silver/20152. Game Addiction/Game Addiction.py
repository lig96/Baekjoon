# 딕 경로(Dyck paths)
#
# 1. dp
# dp[i][j] = dp[i][j-1] + dp[i-1][j]
# 최단 경로는 자명하니 bfs로 별도 탐색을 하지 않아도 된다.
#
# 2. 조합론
# Choose(2n, n)-Choose(2n, n-1) = Choose(2n, n)/(n+1) = 2n! / n! / n+1!
# 참고로 Choose(n, r) = nCr = n! / (n-r)! / r!이다.
# O -> P:=(y=x+1의 첫 교점) -> N의 경로 중
# P -> N 경로를 대칭이동하면 O -> P -> (n-1, n+1)의 경로가 된다.
# 따라서 대각선을 넘어가는 경로는 곧 Choose(2n, n-1)과 일대일대응이다.
# 전체 경우의 수에서 해당 경우의 수만큼 빼주면 된다.
#
# 3. 카탈랑 수
# C0 = 1
# Cn+1 = summation i=0...n(Ci*Cn-i)
# Cn = Choose(2n, n)-Choose(2n, n-1) = Choose(2n, n)/(n+1) = 2n! / n! / n+1!


import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    visited[H][H] = [1, 1]  # 초깃값
    dq.append((H, H))
    while dq:
        r, c = dq.popleft()
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < 31 and 0 <= newc < 31) or (newc > newr):
                continue
            if visited[newr][newc][0] == 0:
                visited[newr][newc][0] = visited[r][c][0]+1
                dq.append((newr, newc))
            # 여기까지 일반 bfs와 코드 동일함.
            if visited[newr][newc][0] == visited[r][c][0]+1:
                # 현재 지점으로부터 방문이 가능하다면
                visited[newr][newc][1] += visited[r][c][1]
                # 경우의 수 증가
    return


H, N = map(int, input().split())


visited = [[[0, 0] for _ in range(31)] for _ in range(31)]
# (최단 거리, 방문의 경우의 수)
dq = deque()
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


bfs()


print(visited[N][N][1])
