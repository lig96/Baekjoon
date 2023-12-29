# 재귀문 대신 반복문으로 제출하여
# PyPy3 2020->1312ms로 약 35%의 시간을 절약했다.
# 기본적으로 반복문이 재귀문보다 빠르다.

# 지역 변수를 쓰는 함수, 매개변수(parameter)을 쓰는 함수는
# 전역 변수를 쓰는 함수, main보다 빠르긴 하다.
# 이번엔 변수가 적어서 재귀문의 디메리트가 더 큰 듯하다.


import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(3e3))


def dfs(r, c):
    visited[r][c] = flood_i
    flood[flood_i][0] += graph[r][c]
    flood[flood_i][1] += 1
    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if not (0 <= newr < N and 0 <= newc < N):
            continue
        if visited[newr][newc] != 0:
            continue
        if not (L <= abs(graph[r][c] - graph[newr][newc]) <= R):
            continue
        dfs(newr, newc)
    return


N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
cnt = 0


while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flood_i = 1
    flood = [[0, 0] for _ in range(N**2+1)]  # [총합, 개수]

    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                dfs(r, c)
                flood_i += 1
            temp_flood = flood[visited[r][c]]
            graph[r][c] = temp_flood[0]//temp_flood[1]

    if flood_i == N**2+1:
        # 1부터 시작해서 N**2를 찍은 뒤 1이 더해졌다면
        # 국경선이 1개도 열리지 않았다면
        break
    else:
        cnt += 1


print(cnt)
