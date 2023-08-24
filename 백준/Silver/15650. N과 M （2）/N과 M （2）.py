def dfs(start, arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(start, N+1):
        dfs(i+1, arr+[i])
N, M = map(int, input().split())
dfs(1, [])