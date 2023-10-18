from itertools import combinations
import sys
input = sys.stdin.readline


def dfs(graph, v, visited):
    r, c = v
    visited[r][c] = True

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if (0 <= nr < N) and (0 <= nc < M) and (graph[nr][nc] == 0):
            graph[nr][nc] = 2
            dfs(graph, (nr, nc), visited)
    return


# 입력
N, M = map(int, input().split())
mat = [x for x in
       ((list(map(int, input().split()))) for _ in range(N))]


# 준비
original_mat = [x[:] for x in mat]
NM = [(row, col) for row in range(N) for col in range(M)]
walls_combis = combinations(NM, 3)
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


# 풀이
ans = 0
for walls in walls_combis:
    # 벽 3개 세우기
    a, b, c = walls
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
    # 중간에 세우면 다음 반복문에서 mat이 더럽혀진 상태임

    # 바이러스 dfs 퍼트리기
    visited = [[False for _ in range(M)] for _ in range(N)]
    for (row, col) in NM:
        if (not visited[row][col]) and (mat[row][col] == 2):
            dfs(mat, (row, col), visited)

    # ans 갱신
    temp_ans = sum([x.count(0) for x in mat])
    if temp_ans > ans:
        ans = temp_ans

    # mat 초기화
    mat = [x[:] for x in original_mat]


# 정답 출력
print(ans)