import sys
input = sys.stdin.readline


def dfs_indegree():
    ans = [0 for _ in range(N+1)]
    # ans[i] = i까지 도달하는 데에 필요한 최대 시간

    qu = []
    for i, v in enumerate(indegree):
        if v == 0:
            qu.append(i)
            ans[i] = D[i]
    while qu:
        now = qu.pop()
        if now == W:
            break
        for end in graph[now]:
            indegree[end] -= 1
            if indegree[end] == 0:
                qu.append(end)
            ans[end] = max(ans[end], ans[now]+D[end])
            # 지금은 indegree가 0이 아니어서 방문을 못 해도
            # 결국 방문할 것이기 때문에 방문한 셈 치고 갱신
    return ans[W]


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    for _ in range(K):
        X, Y = list(map(int, input().split()))
        graph[X].append(Y)
        indegree[Y] += 1
    W = int(input())

    print(dfs_indegree())
