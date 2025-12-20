from collections import deque
import sys
input = sys.stdin.readline


def bfs(N, M, K, board):
    r, c, k = 0, 0, 0
    visited = [[[-1 for _ in range(K+1)]
                for _ in range(M)] for _ in range(N)]
    # visited[r][c][k] = 방문 여부와 최단 거리
    dq = deque()
    visited[r][c][k] = 1  # 시작하는 칸과 끝나는 칸도 포함해서 센다.
    dq.append((r, c, k))

    while dq:
        r, c, k = dq.popleft()
        for i in range(4):
            newr, newc, newk = r+dr[i], c+dc[i], k+1
            if not (0 <= newr < N and 0 <= newc < M):
                continue

            # 벽을 안 부술 때
            if board[newr][newc] == 0 and visited[newr][newc][k] == -1:
                visited[newr][newc][k] = visited[r][c][k] + 1
                dq.append((newr, newc, k))
            # 벽을 부술 때
            if board[newr][newc] == 1 and newk < K+1 and visited[newr][newc][newk] == -1:
                visited[newr][newc][newk] = visited[r][c][k] + 1
                dq.append((newr, newc, newk))

    ret = min(filter(lambda x: x != -1, visited[N-1][M-1]), default=-1)
    return ret


N, M, K = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
# 0은 이동할 수 있는 곳을 나타내고,
# 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


ans = bfs(N, M, K, board)
# (0, 0)에서 (N-1, M-1)로 가는 최단 경로의 길이를 구한다.
# (0, 0), (N-1, M-1)은 항상 0이다.


print(ans)
