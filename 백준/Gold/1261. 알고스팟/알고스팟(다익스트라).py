from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijk(startr, startc):
    dist_mat = [[float('inf') for _ in range(C)] for _ in range(R)]
    heap = []
    dist_mat[startr][startc] = 0
    heappush(heap, (0, startr, startc))

    while heap:
        dist, r, c = heappop(heap)
        if dist_mat[r][c] < dist:
            continue

        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < R and 0 <= newc < C):
                continue
            temp = dist_mat[r][c] + graph[newr][newc]
            if dist_mat[newr][newc] > temp:
                dist_mat[newr][newc] = temp
                heappush(heap, (temp, newr, newc))
    return dist_mat


C, R = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(R)]


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
# visited = [[-1 for _ in range(C)] for _ in range(R)]


dist_mat = dijk(0, 0)


print(dist_mat[R-1][C-1])
