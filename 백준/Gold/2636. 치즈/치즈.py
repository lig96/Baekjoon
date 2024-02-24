import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e4))


def dfs(r, c, visited):
    visited[r][c] = True

    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if not (0 <= newr < R and 0 <= newc < C):
            continue
        if visited[newr][newc]:
            continue
        if graph[newr][newc] == 0:
            # 치즈가 없다면
            dfs(newr, newc, visited)
        else:
            # 치즈가 있다면
            visited[newr][newc] = True
    return


def melt(graph, visited):
    ret = 0
    for r in range(R):
        for c in range(C):
            if graph[r][c] == 1 and visited[r][c]:
                graph[r][c] = 0
                ret += 1
    return ret


R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
old_cnt = sum(graph[r][c] for c in range(C) for r in range(R))


for ans in range(1, int(2e4)):
    visited = [[False for _ in range(C)] for _ in range(R)]
    dfs(0, 0, visited)

    melted_cnt = melt(graph, visited)

    if (cnt := old_cnt-melted_cnt) == 0:
        break
    else:
        old_cnt = cnt


print(ans)
print(old_cnt)
