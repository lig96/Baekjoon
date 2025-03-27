# -1이 방문하지 않았다는 뜻인지 -1만큼의 시간으로 방문했다는 뜻인지
# 구별해야 함. 그래야 min이 제대로 동작함.
# INF로 할 때도 마찬가지.


from collections import deque
import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def new_loc(r, c, k, t):
    for i in range(4):
        yield r+dr[i], c+dc[i], k, t+1
    if k <= K-1:
        for i in range(8):
            yield r+horse_dr[i], c+horse_dc[i], k+1, t+1


def bfs(r, c, k, t):
    visited[r][c][k] = t
    dq.append((r, c, k, t))
    while dq:
        r, c, k, t = dq.popleft()
        for newr, newc, newk, newt in new_loc(r, c, k, t):
            if not (0 <= newr < R and 0 <= newc < C):
                continue
            if not (visited[newr][newc][newk] == -1 or visited[newr][newc][newk] > newt):
                continue
            if board[newr][newc] == 1:
                continue
            visited[newr][newc][newk] = newt
            dq.append((newr, newc, newk, newt))
    return


K = int(input())
C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
# 0은 아무것도 없는 평지, 1은 장애물을 뜻한다.


dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
horse_dr, horse_dc = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]


visited = [[[-1 for _ in range(K+1)] for _ in range(C)] for _ in range(R)]
# -1: 방문하지 않음
# 0 이상의 정수: 방문을 하였고 방문 비용
dq = deque()
bfs(0, 0, 0, 0)


ans = float('inf')
for k in range(K+1):
    if visited[-1][-1][k] != -1:
        ans = min(ans, visited[-1][-1][k])
print(-1 if ans == float('inf') else ans)
