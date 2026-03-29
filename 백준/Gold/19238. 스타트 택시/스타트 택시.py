from collections import deque
import sys
input = sys.stdin.readline


def find_dist(now_pos):
    '''
    now_pos에서 다른 모든 곳으로 가는 최단 거리를 찾는다.
    '''
    dist_arr = [[INF for _ in range(N)] for _ in range(N)]
    dq = deque()
    dist_arr[now_pos[0]][now_pos[1]] = 0
    dq.append(now_pos+[0])

    while dq:
        r, c, d = dq.popleft()
        for i in range(4):
            newr, newc, newd = r+dr[i], c+dc[i], d+1
            if not (0 <= newr < N and 0 <= newc < N):
                continue
            if board[newr][newc] == 1:
                continue
            if newd >= dist_arr[newr][newc]:
                # 이미 방문된 곳이라면
                continue
            dist_arr[newr][newc] = newd
            dq.append([newr, newc, newd])

    return dist_arr


def find_nxt_id(passengers, dist_arr):
    passengers_dist_arr = []
    for i, passenger in enumerate(passengers):
        if passenger[4]:
            continue
        nxt_pos = passenger[0:2]
        temp_dist = dist_arr[nxt_pos[0]][nxt_pos[1]]
        passengers_dist_arr.append((temp_dist, nxt_pos[0], nxt_pos[1], i))

    nxt_passenger = sorted(passengers_dist_arr)[0]
    return nxt_passenger[3]


N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 0은 빈 칸, 1은 벽을 나타낸다.
START_POS = list(map(lambda x: int(x)-1, input().split()))
# 행과 열 번호는 0 이상 N-1 이하의 자연수
passengers = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
# 행과 열 번호는 0 이상 N-1 이하의 자연수


now_pos = START_POS[::]
passengers = [x+[False] for x in passengers]
# passengers: list[list[r, c, r, c, is_moved]]
INF = float('inf')
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


is_broken = False
for _ in range(M):
    dist_arr = find_dist(now_pos)
    nxt_passenger_id = find_nxt_id(passengers, dist_arr)
    nxt_pos = passengers[nxt_passenger_id][0:2]
    dist = dist_arr[nxt_pos[0]][nxt_pos[1]]
    if (dist >= fuel) or (dist == INF):
        # dist == fuel이면 불가능하다.
        is_broken = True
        break
    now_pos = nxt_pos[::]
    fuel -= dist

    passengers[nxt_passenger_id][4] = True

    dist_arr = find_dist(now_pos)
    nxt_pos = passengers[nxt_passenger_id][2:4]
    dist = dist_arr[nxt_pos[0]][nxt_pos[1]]
    if (dist > fuel) or (dist == INF):
        # dist == fuel일 때도 가능하다.
        is_broken = True
        break
    now_pos = nxt_pos[::]
    fuel = fuel - dist + 2*dist


if is_broken:
    print(-1)
else:
    print(fuel)
