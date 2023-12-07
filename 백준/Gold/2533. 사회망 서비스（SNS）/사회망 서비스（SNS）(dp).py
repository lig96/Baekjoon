import sys
sys.setrecursionlimit(int(1e6)+10)
input = sys.stdin.readline


def dfs(start):
    visited[start] = True

    for end in graph[start]:
        if not visited[end]:
            dfs(end)

            dp[start][0] += dp[end][1]
            # start가 ea가 아니라면 end는 무조건 ea여야 함
            # 부분 최적해를 하나씩 더해줌

            dp[start][1] += min(dp[end])
            # start가 ea라면 end가 무엇이든 상관없음
            # 부분 최적해를 하나씩 더해줌
    return


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False for _ in range(N+1)]
dp = [[0, 1] for _ in range(N+1)]
# [자기 자신이 ea가 아닐 때 정답, ea일 때 정답]

dfs(1)  # 아무 노드에서 시작해도 무방


print(min(dp[1]))
