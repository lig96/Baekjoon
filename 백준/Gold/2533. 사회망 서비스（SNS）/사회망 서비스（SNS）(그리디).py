import sys
sys.setrecursionlimit(int(1e6)+10)
input = sys.stdin.readline


def dfs(start):
    visited[start] = True

    for end in graph[start]:
        if not visited[end]:
            dfs(end)
            if not ans[end]:
                # 차일드가 얼리어답터가 아니라면
                # 자신이 얼리어답터여야 함
                ans[start] = True
    return


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


ans = [False for _ in range(N+1)]
visited = [False for _ in range(N+1)]
dfs(1)  # 아무 노드에서 시작해도 무방


print(sum(ans))
