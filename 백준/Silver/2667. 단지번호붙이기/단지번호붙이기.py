def dfs(graph, rc, level):
    r, c = rc
    graph[r][c] = '0'
    for i in range(4):
        newr, newc = r+dx[i], c+dy[i]
        if (0 <= newr < N) and (0 <= newc < N):
            if graph[newr][newc] == '1':
                level = dfs(graph, (newr, newc), level+1)
    return level


N = int(input())
graph = []
for _ in range(N):
    temp = list(input())
    graph.append(temp)
total = 0
each = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for row in range(N):
    for col in range(N):
        if graph[row][col] == '1':
            level = dfs(graph, (row, col), 1)
            if level > 0:
                total += 1
                each.append(level)

print(total)
print(*sorted(each), sep='\n')
