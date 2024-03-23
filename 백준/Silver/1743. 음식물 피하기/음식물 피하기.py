import sys
input = sys.stdin.readline


def dfs(startr, startc):
    graph[startr][startc] = False
    stack = [(startr, startc)]
    ret = 1

    while stack:
        r, c = stack.pop()
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if 0 <= newr < R and 0 <= newc < C and graph[newr][newc]:
                graph[newr][newc] = False
                stack.append((newr, newc))
                ret += 1

    return ret


R, C, K = map(int, input().split())
graph = [[False for _ in range(C)] for _ in range(R)]
for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = True
    # 제로 인덱싱


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


ans = -1
for r in range(R):
    for c in range(C):
        if graph[r][c]:
            temp_ans = dfs(r, c)
            ans = max(ans, temp_ans)


print(ans)
