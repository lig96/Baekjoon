import sys
input = sys.stdin.readline


def spread():
    new_graph = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            new_graph[r][c] += graph[r][c]
            if graph[r][c] <= 0:
                continue
            amount = graph[r][c]//5
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1:
                    new_graph[nr][nc] += amount
                    new_graph[r][c] -= amount
    return new_graph


def clean(type, rc):
    r, c = rc
    if type == 'upper':
        dr = [0, -1, 0, 1]
        dc = [1, 0, -1, 0]
        # 오른쪽, 위쪽, 왼쪽, 아래쪽
    elif type == 'lower':
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        # 오른쪽, 아래쪽, 왼쪽, 위쪽

    before = 0
    for i in range(4):
        while True:
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1:
                # 일직선으로 쭉 가는 것의 탈출 조건은
                # 벽에 부딪히거나, 한 바퀴 돌고 에어컨에 부딪힐 때
                graph[nr][nc], before = before, graph[nr][nc]
                r, c = nr, nc
            else:
                break


R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]


dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
cleaners = [(r, 0) for r in range(R) if graph[r][0] == -1]


for _ in range(T):
    graph = spread()
    clean('upper', cleaners[0])
    clean('lower', cleaners[1])


ans = sum(map(sum, graph)) + 2
print(ans)
