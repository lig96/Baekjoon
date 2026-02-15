import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


ans = 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            continue
        ans += 2  # 윗면, 아랫면
        for i in range(4):
            # 왼쪽 면, 오른쪽 면, 앞쪽 면, 뒷쪽 면
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < N and 0 <= newc < M):
                # 현재가 가장 자리라면
                height_of_neighbor = 0
            else:
                height_of_neighbor = board[newr][newc]
            diff = board[r][c] - height_of_neighbor
            if diff <= 0:
                # 지금 칸이 같은 높이거나 더 낮은 높이라면
                continue
            ans += diff


print(ans)
