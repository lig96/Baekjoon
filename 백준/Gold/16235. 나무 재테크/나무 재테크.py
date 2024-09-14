# do_sp, do_sum, do_fall, do_win 함수 4개
# 무한한 1차원 배열에 (r, c, z). PyPy3 - 1172ms
# N*N 2차원 배열에 (z). PyPy3 - 752ms
#
# do_sp, do_sum_fall_win 함수 2개
# 무한한 1차원 배열에 (r, c, z). PyPy3 - 안해봄
# N*N 2차원 배열에 z. PyPy3 - 564ms
#
# 위는 모두 deque 사용 기준이고
# 딕셔너리로 나무의 크기별 개수 관리하고 정렬은 key만 정렬하면 200ms까지 가능


from collections import deque
import sys
input = sys.stdin.readline


def do_spring():
    for r, c in range_rc:
        now_trees = trees[r][c]
        for _ in range(len(now_trees)):
            z = now_trees.popleft()
            if land[r][c] >= z:
                land[r][c] -= z
                now_trees.append(z+1)
            else:
                dead_trees[r][c] += z//2
    return


def do_summer_fall_winter():
    for r, c in range_rc:
        # fall
        now_trees = trees[r][c]
        for z in now_trees:
            # 자기 자신에게는 나무가 안 생기기 때문에 임시 복사 없이 해도 됨
            if z % 5 != 0:
                continue
            for i in range(8):
                newr, newc = r+dr[i], c+dc[i]
                if not (0 <= newr < N and 0 <= newc < N):
                    continue
                trees[newr][newc].appendleft(1)  # appendleft, 오름차순 유지
        # summer, winter
        land[r][c] += A_arr[r][c] + dead_trees[r][c]
        dead_trees[r][c] = 0
    return


N, M, K = map(int, input().split())
land = [[5 for _ in range(N)] for _ in range(N)]  # 시작값 5
A_arr = [list(map(int, input().split())) for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)  # zero-indexing
# 첫 입력은 동일 위치에 나무가 생기지 않기 때문에
# 각 좌표마다 따로 데큐를 만들었으면 정렬할 필요 없음
dead_trees = [[0 for _ in range(N)] for _ in range(N)]


dr, dc = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
range_rc = [(r, c) for r in range(N) for c in range(N)]
# 제너레이터 익스프레션은 일회용이라 안 되고 리스트, 튜플, 제너레이터 함수 써야 함


for _ in range(K):
    do_spring()
    do_summer_fall_winter()


ans = 0
for r, c in range_rc:
    ans += len(trees[r][c])


print(ans)
