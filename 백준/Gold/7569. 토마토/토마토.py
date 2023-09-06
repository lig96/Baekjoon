from collections import deque
from sys import stdin
input = stdin.readline


M, N, H = map(int, input().split())
mat = [[list(map(int, input().split())) for _ in range(N)]
       for _ in range(H)]
# mat[H, height][N, row][M, col]
cnt = 0
qu = deque()
for m in range(M):
    for n in range(N):
        for h in range(H):
            if mat[h][n][m] == 0:
                cnt += 1
            elif mat[h][n][m] == 1:
                qu.append((h, n, m, 0))
dh = [0, 0, 1, -1, 0, 0]
dn = [1, -1, 0, 0, 0, 0]
dm = [0, 0, 0, 0, 1, -1]


while qu:
    h, n, m, day = qu.popleft()
    for i in range(6):
        nh, nn, nm = h+dh[i], n+dn[i], m+dm[i]
        if (0 <= nh < H) and (0 <= nn < N) and (0 <= nm < M):
            if mat[nh][nn][nm] == 0:
                mat[nh][nn][nm] = 1
                qu.append((nh, nn, nm, day+1))
                cnt -= 1


print(day) if cnt == 0 else print(-1)