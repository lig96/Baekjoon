import sys
from itertools import combinations


def dfs(graph, v, visited):
    r, c = v
    visited[r][c] = True

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]

        if not ((0 <= nr < N) and (0 <= nc < M)):
            continue
        if not ((graph[nr][nc] == 0)):
            continue
        if not (not visited[nr][nc]):
            continue
        graph[nr][nc] = 2
        dfs(graph, (nr, nc), visited)
    return


input = sys.stdin.readline


N, M = map(int, input().split())
mat = [x for x in
       ((list(map(int, input().split()))) for _ in range(N))]


original_mat = [x[:] for x in mat]
NM = [(row, col) for row in range(N) for col in range(M)]
combis = combinations(NM, 3)
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

ans = 0
for a, b, c in combis:
    # if (a, b, c) == ((0, 1), (1, 0), (3, 5)):
    #     print('hi')
    #     print(*mat, sep='\n')

    if mat[a[0]][a[1]] != 0:
        continue
    if mat[b[0]][b[1]] != 0:
        continue
    if mat[c[0]][c[1]] != 0:
        continue
    mat[a[0]][a[1]] = 1
    mat[b[0]][b[1]] = 1
    mat[c[0]][c[1]] = 1
    # 벽을 세울 공간이 비어있지 않다면 continue
    # (continue 다 끝난 다음에) 비어있다면 벽을 세움

    visited = [[False for _ in range(M)] for _ in range(N)]
    for (row, col) in NM:
        if (not visited[row][col]) and mat[row][col] == 2:
            dfs(mat, (row, col), visited)

    num_2 = sum([x.count(0) for x in mat])
    if num_2 > ans:
        ans = num_2

    mat = [x[:] for x in original_mat]
print(ans)
