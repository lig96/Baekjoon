# make_adj_list = O(N^2)
# bfs = O(V+E) = O(N^2)


from collections import deque
import sys
input = sys.stdin.readline


def make_adj_list(N, areas):
    def can_communicate(left, right):
        x1, y1, r1 = left
        x2, y2, r2 = right

        if ((x1-x2)**2 + (y1-y2)**2) <= (r1+r2)**2:
            # 둘 다 제곱한 형태
            return True
        else:
            return False

    adj_list = [[] for _ in range(N)]

    for left_i in range(0, N-1):
        left = areas[left_i]
        for right_i in range(left_i+1, N):
            right = areas[right_i]
            if can_communicate(left, right):
                adj_list[left_i].append(right_i)
                adj_list[right_i].append(left_i)
    return adj_list


def bfs(graph, visited, startx, flood_fill_i):
    visited[startx] = flood_fill_i
    qu = deque([startx])

    while qu:
        x = qu.popleft()
        for nxt in adj_list[x]:
            if visited[nxt] == -1:
                visited[nxt] = flood_fill_i
                qu.append(nxt)
    return


T = int(input())
for _ in range(T):
    N = int(input())
    areas = [list(map(int, input().split())) for _ in range(N)]
    # x, y, R

    adj_list = make_adj_list(N, areas)

    visited = [-1 for _ in range(N)]
    flood_fill_i = 0
    for startx in range(N):
        if visited[startx] == -1:
            bfs(adj_list, visited, startx, flood_fill_i)
            flood_fill_i += 1



    print(flood_fill_i)
