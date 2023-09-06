N = int(input())
graph = []
INF = int(1e9)
for i in range(N):
    temp = list(map(lambda x: INF if x == '0' else 1, input().split()))
    graph.append(temp)


for k in range(N):
    for a in range(N):
        for b in range(N):
            old = graph[a][b]
            new = graph[a][k] + graph[k][b]
            if new < old:
                graph[a][b] = new


for i in range(N):
    for j in range(N):
        if graph[i][j] < INF:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
