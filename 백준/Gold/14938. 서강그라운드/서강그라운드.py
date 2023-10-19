def f_w():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return


n, m, r = map(int, input().split())
t_arr = [0]+list(map(int, input().split()))
INF = int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l
for i in range(1, n+1):
    graph[i][i] = 0


f_w()


ans = 0
for costs in graph:
    temp_ans = sum([(costs[i] <= m) * t_arr[i] for i in range(1, n+1)])
    if temp_ans > ans:
        ans = temp_ans
print(ans)
