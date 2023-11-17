import sys
input = sys.stdin.readline


def dfs(r, c):
    visited[r][c] = now_cycle
    # now_cycle.add((r,c))

    i = dir_to_i[graph[r][c]]
    newr, newc = r+dr[i], c+dc[i]
    if not visited[newr][newc]:
        return dfs(newr, newc)
    else:
        if visited[newr][newc] == now_cycle:
            # 현재 dfs가 현재 사이클을 만듦
            return 1
        else:
            # 현재 dfs가 과거 사이클에 도달함
            return 0


N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

if N == 1 and M == 1:
    raise Exception

visited = [[False for _ in range(M)] for _ in range(N)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
dir_to_i = {'U': 0, 'D': 1, 'L': 2, 'R': 3}


ans = 0
now_cycle = 0
for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            now_cycle = now_cycle + 1  # visited 배열의 서로 다른 값
            # now_cycle = set()
            ans += dfs(r, c)


print(ans)
