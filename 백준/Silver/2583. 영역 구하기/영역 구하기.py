from collections import defaultdict
import sys
input = sys.stdin.readline


def condition(r, c):
    if not (0 <= r < R and 0 <= c < C):
        return False
    if not (visited[r][c] == -1):
        return False
    if not (not is_colored[r][c]):
        return False
    return True


def dfs(startr, startc):
    def update(r, c):
        visited[r][c] = flood_fill_i
        flood_dic[flood_fill_i] += 1
        stack.append((r, c))
        return
    stack = []
    update(startr, startc)

    while stack:
        r, c = stack.pop()
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if condition(newr, newc):
                update(newr, newc)
    return


R, C, K = map(int, input().split())
is_colored = [[False for _ in range(C)] for _ in range(R)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for c in range(x1, x2):
        for r in range(y1, y2):
            is_colored[r][c] = True
# '왼쪽 아래 꼭짓점의 x, y좌표값과
# 오른쪽 위 꼭짓점의 x, y좌표값이'
# -> 따라서 x1<=x2, y1<=y2 보장됨.


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


visited = [[-1 for _ in range(C)] for _ in range(R)]
flood_fill_i = 0
flood_dic = defaultdict(lambda: int(0))
for r in range(R):
    for c in range(C):
        if condition(r, c):
            dfs(r, c)
            flood_fill_i += 1


print(len(flood_dic))
print(*sorted(flood_dic.values()))
