import sys
input = sys.stdin.readline


def bisect_right():
    lo, hi = 1, 1_000_000_000+1
    while lo < hi:
        mid = (lo+hi)//2
        if dfs(mid):
            lo = mid+1
        else:
            hi = mid
    return lo


def dfs(mid):
    stack = []
    visited = [False for _ in range(N+1)]
    stack.append(input_S)
    visited[input_S] = True
    while stack:
        x = stack.pop()
        for child, c in graph[x]:
            if visited[child] or mid > c:
                continue
            stack.append(child)
            visited[child] = True
    return visited[input_E]


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))
    graph[b].append((a, c))
# A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다.
# 서로 같은 두 섬 사이에 여러 개의 다리가 있을 수도 있으며,
# 모든 다리는 양방향이다.
# 아마 원인덱싱.
input_S, input_E = map(int, input().split())


ans = bisect_right()


print(ans-1)
