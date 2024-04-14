# 백트래킹
#
# 현재 경로에서 방문이 되었으면, 라인 A 때문에 재귀를 들어가지 않고
# 현재 경로가 아닌 경로에서 방문이 되었으면,
# 경로를 마친 뒤 원상복귀 되었기 때문에 라인 A 이후 재귀를 들어간다.
#
# 원상복귀가 되었다는 것은 visited가 해당 시점의 상태로 다시 돌아간다는 것이다.


import sys
input = sys.stdin.readline
# sys.setrecursionlimit(3000)  # 애초에 재귀가 5만 들어가도 정답이라 필요없음


def dfs(x, d):
    if d == 5:
        global ans
        ans = 1
        return

    visited[x] = True
    for newx in graph[x]:
        if not visited[newx]:  # 라인 A
            dfs(newx, d+1)
    visited[x] = False
    # 다시 원상복귀
    return


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


ans = 0
visited = [False for _ in range(N)]
# 자동으로 원상복귀돼서 반복문 내에서 새로 초기화 안 해도 됨
for x in range(N):
    if not visited[x]:  # 언제나 참
        dfs(x, 1)

    if ans == 1:
        break


print(ans)
