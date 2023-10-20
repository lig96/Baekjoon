import sys
input = sys.stdin.readline


R, C, T = map(int, input().split())
graph = [x for x in
         (list(map(int, input().split())) for _ in range(R))]

# print(*graph, sep='\n')


dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]


def spread():
    new_graph = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if graph[r][c] == 0:
                continue
            elif graph[r][c] == -1:
                new_graph[r][c] = -1
                continue

            can_dirs = 0
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1:
                    can_dirs += 1
            spread_amount = graph[r][c] // 5
            remain_amount = graph[r][c] - can_dirs*spread_amount

            new_graph[r][c] += remain_amount
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1:
                    new_graph[nr][nc] += spread_amount
    return new_graph


def clean():
    flag_next_cleaner = 'upper'
    for r in range(R):
        for c in range(C):
            if not (graph[r][c] == -1):
                continue
            if flag_next_cleaner == 'upper':
                before = 0
                for nc in range(1, C):
                    graph[r][nc], before = before, graph[r][nc]
                    # 오른쪽
                for nr in range(r-1, -1, -1):
                    graph[nr][-1], before = before, graph[nr][-1]
                    # 위쪽
                for nc in range(C-1-1, -1, -1):
                    graph[0][nc], before = before, graph[0][nc]
                    # 왼쪽
                for nr in range(1, r):
                    graph[nr][0], before = before, graph[nr][0]
                    # 아래쪽
                flag_next_cleaner = 'lower'
            elif flag_next_cleaner == 'lower':
                before = 0
                for nc in range(1, C):
                    graph[r][nc], before = before, graph[r][nc]
                    # 오른쪽
                for nr in range(r+1, R):
                    graph[nr][-1], before = before, graph[nr][-1]
                    # 아래쪽
                for nc in range(C-1-1, -1, -1):
                    graph[-1][nc], before = before, graph[-1][nc]
                    # 왼쪽
                for nr in range(R-1-1, r, -1):
                    graph[nr][0], before = before, graph[nr][0]
                    # 위쪽
                flag_next_cleaner = 'no next clear'
    return graph


for _ in range(T):
    graph = spread()
    clean()

ans = sum([sum(x) for x in graph])+2
print(ans)
