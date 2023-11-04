# 깊이를 저장할 필요가 있다면 visited 배열을 이용하자.


from collections import deque


def bfs(graph, sr, sc):
    qu = deque()
    qu.append((sr, sc))
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[sr][sc] = 0
    at_least_one_fish = False

    while qu:
        r, c = qu.popleft()

        if at_least_one_fish and visited[r][c] > at_least_one_fish:
            # 깊이 3에서 찾았으면 깊이 4 물고기는 안 찾아도 됨
            break

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                fish = graph[nr][nc]
                if fish > shark:
                    pass
                elif fish == shark:
                    qu.append((nr, nc))
                    visited[nr][nc] = visited[r][c]+1
                else:  # fish < shark
                    if fish == 0:  # 빈 공간
                        qu.append((nr, nc))
                        visited[nr][nc] = visited[r][c]+1
                    else:  # fish 존재
                        qu.append((nr, nc))
                        visited[nr][nc] = visited[r][c]+1
                        foods.append((nr, nc, visited[nr][nc]))
                        if not at_least_one_fish:
                            at_least_one_fish = visited[nr][nc]
    return


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


for r in range(N):
    for c in range(N):
        if graph[r][c] == 9:
            sr, sc = r, c
            graph[r][c] = 0  # 9는 상어의 위치일 뿐이니 필요 없음


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
shark, shark_stomach = 2, 0


ans = 0
while True:
    foods = []
    bfs(graph, sr, sc)

    if foods:
        foods.sort(key=lambda x: (x[2], x[0], x[1]))  # depth, r, c 순서
        sr, sc, depth = foods[0]  # 상어 이후 자리 선언
        graph[sr][sc] = 0  # 물고기 이전 자리 초기화
        shark_stomach += 1
        if shark == shark_stomach:
            shark += 1
            shark_stomach = 0
        ans += depth
    else:
        print(ans)
        break
