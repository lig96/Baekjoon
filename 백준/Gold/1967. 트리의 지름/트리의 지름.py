import sys
input = sys.stdin.readline


def dfs(graph_, v, visited):
    stack = []
    stack.append((v, 0))
    visited[v] = True
    ans1, ans2 = 0, 0

    while stack:
        now, now_c = stack.pop()
        for i in graph[now]:
            child, c = i
            if not visited[child]:
                visited[child] = True
                stack.append((child, now_c+c))
                if now_c+c > ans2:
                    ans1, ans2 = child, now_c+c
    return ans1, ans2


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, c = map(int, input().split())
    graph[parent].append((child, c))
    graph[child].append((parent, c))
    # 양방향

furthest_A, _ = dfs(None, 1, [False for _ in range(n+1)])
furthest_B, ans = dfs(None, furthest_A, [False for _ in range(n+1)])
print(ans)