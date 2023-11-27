from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write


def bfs(graph, rc, visited):
    qu = deque()
    area_len = 0

    qu.append(rc)
    visited[rc[0]][rc[1]] = area_i
    area_len += 1
    area_len %= 10

    while qu:
        r, c = qu.popleft()
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if 0 <= newr < N and 0 <= newc < M and not visited[newr][newc] and graph[newr][newc] == 0:
                qu.append((newr, newc))
                visited[newr][newc] = area_i
                area_len += 1
                area_len %= 10
    return area_len


N, M = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[False for _ in range(M)] for _ in range(N)]
area_i = 1
area_to_len = dict()


# visited 배열을 area의 인덱스로 갱신하고
# 딕셔너리로 인덱스-길이를 매칭시켜줌
for r in range(N):
    for c in range(M):
        if graph[r][c] == 0 and not visited[r][c]:
            area_to_len[area_i] = bfs(graph, (r, c), visited)
            area_i += 1

# 상하좌우 중 중복되는 area의 인덱스를 제외하고
# area의 길이를 더해줌
for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            areas = set()
            for i in range(4):
                newr, newc = r+dr[i], c+dc[i]
                if 0 <= newr < N and 0 <= newc < M and visited[newr][newc]:
                    areas.add(visited[newr][newc])

            ans = 1
            for area_i in areas:
                ans += area_to_len[area_i]
                
            print(str(ans % 10))
        else:
            print(str(0))
    print('\n')
