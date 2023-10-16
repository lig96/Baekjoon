import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c
for i in range(n+1):
    graph[i][i] = 0


def f_w():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]


f_w()


for i in range(1, n+1):
    for j in range(1, n+1):
        temp = graph[i][j]
        print(temp, end=' ') if temp < INF else print(0, end=' ')
    print()