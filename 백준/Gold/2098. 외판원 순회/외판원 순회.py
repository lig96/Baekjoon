import sys
input = sys.stdin.readline


def dfs(start, visited):
    if visited == (1 << N)-1:
        if graph[start][0] != 0:
            return graph[start][0]
        else:
            return float('inf')

    if dp[start][visited] != 'not visited':
        # 0123과 0213은 사실상 동일하고
        # 둘 다 dp[3][0b1111]으로 잡힘
        return dp[start][visited]

    min_dist = float('inf')
    for end in range(N):
        if visited & (1 << end):
            # 이미 방문한 경우
            continue
        if graph[start][end] == 0:
            # 방문할 수 없는 경우
            continue
        temp = dfs(end, visited | (1 << end)) + graph[start][end]
        if min_dist > temp:
            min_dist = temp
    dp[start][visited] = min_dist
    return dp[start][visited]


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# graph[start][end] = cost


dp = [['not visited' for _ in range(1 << N)] for _ in range(N)]
# dp[마지막으로 방문한 도시][총 방문한 도시]인 상태에서
# 순회를 끝마쳤을 때 방문 비용의 최솟값
#
# <점화식> dp[0] = 그 다음 도시들의 값들 중 최솟값
#
# 해당 값이 INF더라도 방문을 한 상태에서 INF가 나온 거라면
# 그 값을 활용해야 하기 때문에
# 초기값을 INF로 하면 안 된다.
# 방문한 INF, 방문 안 한 INF는 서로 달라야 함.


print(dfs(0, 1 << 0))
