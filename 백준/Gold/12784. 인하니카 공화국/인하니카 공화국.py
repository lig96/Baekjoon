import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e3)+100)


def sol(N, M, graph):
    dp = [[None, None] for _ in range(N)]
    # dp[n] = (n != 리프 노드)
    #       [n번째 섬의 위로의 다리 1개를 끊는 비용,
    #       n번째 섬의 아래의 섬들과 연결이 모두 끊어지는 비용]
    # dp[n] = (n == 리프 노드)
    #       [n번째 섬의 위로의 다리 1개를 끊는 비용,
    #       float('inf')]
    # dp[parent] = [다이너마이트 비용,
    #               sum(min(dp[child]) for child in graph[parent])

    visited = [False for _ in range(N)]
    dfs(0, graph, dp, visited)

    return dp[0][1]  # [None, 4]


def dfs(x, graph, dp, visited):
    visited[x] = True

    temp = 0
    for child, cost in graph[x]:
        if not visited[child]:
            dp[child][0] = cost
            dfs(child, graph, dp, visited)  # dp[child][1]
            temp += min(dp[child])

    # dp[x][0]은 parent 단계에서 대입됨.
    dp[x][1] = temp if temp or x == 0 else float('inf')
    # 1번 섬이 아니고 다리가 1개인 섬이라면 temp=0이 아닌 기본값 INF를 대입해야 함.
    return


for _ in range(T := int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1  # 제로인덱싱
        graph[a].append((b, c))  # 양방향
        graph[b].append((a, c))  # 양방향

    ans = sol(N, M, graph)

    print(ans)
