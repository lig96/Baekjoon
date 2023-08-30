N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))


def dfs(start, level, char):
    if level == M+1:
        print(*char)
        return
    for i in range(start, N):
        dfs(i, level+1, char+[num[i]])


dfs(0, 1, [])
