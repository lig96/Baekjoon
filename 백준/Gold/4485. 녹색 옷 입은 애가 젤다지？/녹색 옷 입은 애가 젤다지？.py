from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijk(startrc):
    startr, startc = startrc
    dist_arr = [[INF for c in range(N)] for r in range(N)]
    heap = []
    dist_arr[startr][startc] = cave[startr][startc]
    heappush(heap, (dist_arr[startr][startc], startrc))

    while heap:
        now_dist, (r, c) = heappop(heap)
        if dist_arr[r][c] < now_dist:
            continue
        if (r, c) == (N-1, N-1):
            break

        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < N and 0 <= newc < N):
                continue
            nxt_dist = cave[newr][newc]

            temp = now_dist+nxt_dist
            if dist_arr[newr][newc] > temp:
                dist_arr[newr][newc] = temp
                heappush(heap, (dist_arr[newr][newc], (newr, newc)))
    return dist_arr


for tc in range(1, int(1e6)):
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]

    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    INF = float('inf')

    dist_arr = dijk((0, 0))

    print(f'Problem {tc}: {dist_arr[N-1][N-1]}')
