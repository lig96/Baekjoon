# 라이브러리
from collections import deque
import sys
input = sys.stdin.readline


# 함수
def bfs(start, visited):
    tot_candy = 0
    tot_ppl = 0

    tot_candy += candies[start]
    tot_ppl += 1
    visited[start] = True
    qu = deque([start])

    while qu:
        now = qu.popleft()
        for end in graph[now]:
            if not visited[end]:
                tot_candy += candies[end]
                tot_ppl += 1
                visited[end] = True
                qu.append(end)
    return (tot_candy, tot_ppl)


def make_cycles():
    visited = [False for _ in range(N+1)]
    cycles = []
    for start in range(1, N+1):
        if not visited[start]:
            cycle = bfs(start, visited)
            cycles.append(cycle)
    return cycles


# 입력
N, M, K = map(int, input().split())
candies = ['default'] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 준비
cycles = make_cycles()
dp = [0 for _ in range(3_000+1)]  # 거꾸로 접근하는 1차원 인덱싱


# 풀이
for cycle in range(len(cycles)):
    now_candy, now_ppl = cycles[cycle]
    for ppl in range(3_000, -1, -1):
        if ppl < now_ppl:
            dp[ppl] = dp[ppl]
        else:
            dp[ppl] = max(
                dp[ppl],
                dp[ppl-now_ppl]+now_candy
            )


# 출력
print(dp[K-1])
