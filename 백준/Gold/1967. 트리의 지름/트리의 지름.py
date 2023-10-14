# 풀이 1. 플로이드-워셜 알고리즘
# 공간복잡도 V^2, 시간복잡도 V^3 -> 시간 초과

# 풀이 2. 길찾기 n번
# dfs, bfs를 통해 구한 리프 노드 n개 혹은 전체 노드 V개에 대해서 길찾기
# 웬만하면 시간 초과

# 풀이 3. 길찾기 2번
# https://blog.myungwoo.kr/112
# 1. 트리에서 임의의 정점 x를 잡는다.
# 2. 정점 x에서 가장 먼 정점 y를 찾는다.
# 3. 정점 y에서 가장 먼 정점 z를 찾는다.
# 가중치가 있는 그래프에서는 다익스트라를 써야하지만
# 순환 구조(=특정 노드로의 접근 방법이 2가지 이상)가 없는 트리에서는
# dfs를 써도 무방하고 더 빠르다.
# O(V+E) vs O(E+ElogE)


import sys
input = sys.stdin.readline


def dfs(graph, v, visited):
    stack = []
    stack.append((v, 0))
    visited[v] = True
    ans1, ans2 = 0, 0

    while stack:
        now, now_c = stack.pop()

        for i in graph[now]:
            child, c = i
            if not visited[child]:
                stack.append((child, now_c+c))
                visited[child] = True
                if now_c+c > ans2:
                    ans1, ans2 = child, now_c+c
    return ans1, ans2


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, c = map(int, input().split())
    graph[parent].append((child, c))
    graph[child].append((parent, c))


furthest_A, _ = dfs(graph, 1, [False for _ in range(n+1)])
furthest_B, ans = dfs(graph, furthest_A, [False for _ in range(n+1)])


print(ans)
