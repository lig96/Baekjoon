import copy
from collections import deque


N = int(input())
graph1 = [list(input()) for _ in range(N)]
graph2 = copy.deepcopy(graph1)
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
dic1 = {'R': 'R', 'G': 'G', 'B': 'B'}
dic2 = {'R': 'RG', 'G': 'RG', 'B': 'B'}
cnt_arr = [0, 0]


def bfs(graph, v, dic, num):
    row, col = v
    if graph[row][col] == 'V':
        return
    color = dic[graph[row][col]]
    graph[row][col] = 'V'
    qu = deque([(row, col)])
    cnt_arr[num] += 1

    while qu:
        nowr, nowc = qu.popleft()
        for i in range(4):
            newr, newc = nowr+dr[i], nowc+dc[i]
            if (0 <= newr < N) and (0 <= newc < N):
                if graph[newr][newc] in color:
                    graph[newr][newc] = 'V'
                    qu.append((newr, newc))
    return


for row in range(N):
    for col in range(N):
        bfs(graph1, (row, col), dic1, 0)
        bfs(graph2, (row, col), dic2, 1)


print(*cnt_arr)