# 방법 1.
# flood-fill을 통해 섬들을 구분하고
# bfs를 통해 육지 a에서 다른 인덱스의 육지에 도착할 때의
# 거리를 구한다.
# Python 3 88ms, PyPy3 180ms
# c++ 4ms https://forward-gradually.tistory.com/68

# 방법 2.
# flood-fill을 통해 섬들을 구분하고
# 모든 육지를 저장 후 조합과 맨하탄 거리를 통해
# 거리를 구한다.
# Python 3 6268, PyPy3 604ms
# c++ 48ms https://forward-gradually.tistory.com/68

# 육지 a와 다른 육지 100개가 있을 때
# 방법 1은 육지 a-가장 가까운 육지를 구하고 끝나는데
# 방법 2는 육지 a-100개의 육지를 모두 구한다.
# 시행 한 번의 시간 복잡도가 O(V+E), O(1)이긴 하나
# 방법 1의 시행 횟수는 언제나 1번이고
# 찾으면 곧바로 멈추니 최악일 때인 O(V+E)보다 같거나 낫고
# 방법 2의 시행 횟수는 언제나 전체 경우이니 100 * O(1)이다.
# 따라서 오히려 방법 1이 빠르다.


from collections import deque
import sys
input = sys.stdin.readline


def bfs_floodfill(startr, startc):
    qu = deque()
    qu.append((startr, startc))
    visited[startr][startc] = flood

    while qu:
        r, c = qu.popleft()
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < N and 0 <= newc < N):
                continue
            if visited[newr][newc]:
                continue
            if graph[newr][newc] == 0:
                continue
            qu.append((newr, newc))
            visited[newr][newc] = flood
    return


def bfs_finddist(target, startr, startc):
    qu = deque()
    qu.append((startr, startc))
    new_v[startr][startc] = 0

    while qu:
        r, c = qu.popleft()
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < N and 0 <= newc < N):
                continue
            if new_v[newr][newc] != -1:
                continue

            if graph[newr][newc] == 1 and visited[newr][newc] != target:
                return new_v[r][c]
            qu.append((newr, newc))
            new_v[newr][newc] = new_v[r][c]+1
    return


def near_water(r, c):
    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if not (0 <= newr < N and 0 <= newc < N):
            continue
        if graph[newr][newc] == 0:
            return True
    return False


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[False for _ in range(N)] for _ in range(N)]
flood = 1
areas = []
ans = float('inf')


# flood-fill, 육지를 배열에 저장
for r in range(0, N):
    for c in range(0, N):
        if not visited[r][c] and graph[r][c] == 1:
            bfs_floodfill(r, c)
            flood += 1
        if visited[r][c] and near_water(r, c):
            areas.append((visited[r][c], r, c))

# 육지마다 가장 가까운 다른 섬 탐색
for flood_i, r, c in areas:
    new_v = [[-1 for _ in range(N)] for _ in range(N)]
    dist = bfs_finddist(flood_i, r, c)
    if ans > dist:
        ans = dist
        if ans == 1:
            break
# 방법 2.
# for left_i in range(1, flood):
#     for right_i in range(left_i+1, flood):
#         for left in areas[left_i]:
#             for right in areas[right_i]:
#                 ans = min(ans, find_dist(left, right))


print(ans)
