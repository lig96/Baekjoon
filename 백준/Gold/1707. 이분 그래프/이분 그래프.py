# 전역 변수 ans 문자열을 따로 두지 않고
# 지금처럼 함수의 return 값을 활용할 수도 있다.
# 구현이 어렵지만 약간이나마 빠르고 함수 내에서 해결이 가능하다.


import sys
sys.setrecursionlimit(int(3e4))
input = sys.stdin.readline


def dfs(v, group):
    if visited[v] == -1:
        # 방문이 안 되었다면
        visited[v] = group  # group 초기값 False
        for node in edges[v]:
            temp = dfs(node, not group)  # False, True 번갈아
            if temp == 'NO':
                return 'NO'
        return 'YES'
    else:
        # 방문이 되었다면
        if visited[v] == group:
            return 'YES'
        else:
            return 'NO'


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = list(map(int, input().split()))
        edges[u].append(v)
        edges[v].append(u)

    visited = [-1 for _ in range(V+1)]

    for start_v in range(1, V+1):
        if visited[start_v] == -1:
            ans = dfs(start_v, False)
            if ans == 'NO':
                break

    print(ans)
