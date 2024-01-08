import sys
input = sys.stdin.readline


def dfs():
    while stack:
        r, c = stack.pop()
        if visited[r][c]:
            continue
        visited[r][c] = True

        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < R and 0 <= newc < C):
                continue
            if visited[newr][newc]:
                continue

            if graph[newr][newc] == 1:
                new_stack.append((newr, newc))
            else:
                # visited[newr][newc] = True
                stack.append((newr, newc))
    return


C, R = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(R)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[False for _ in range(C)] for _ in range(R)]


stack, new_stack = [(0, 0)], []
for broken_wall_cnt in range(0, C*R+1):
    dfs()

    if visited[R-1][C-1]:
        break
    else:
        stack, new_stack = new_stack, []


print(broken_wall_cnt)
