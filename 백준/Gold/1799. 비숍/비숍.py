

import sys
input = sys.stdin.readline


def dfs(r, local_ans, graph):
    global ans

    if r == 2*N-1:
        # 깊이를 끝까지 간 경우
        if ans < local_ans:
            ans = local_ans
        return

    # 깊이가 끝이 아닌 경우
    if (local_ans + ((2*N-1)-r)) <= ans:
        # 끝까지 가도 갱신이 불가능한 경우
        return
    # 끝까지 가면 아마도 갱신이 가능한 경우
    for c in graph[r]:
        if visited_c[c]:
            # 세로줄을 이미 썼을 경우
            continue
        # 언제나 visited_r[r]은 False

        visited_c[c] = True
        dfs(r+1, local_ans+1, graph)
        visited_c[c] = False
    dfs(r+1, local_ans, graph)
    # 현재 row에서는 아무 칸도 안 쓰고 다음 깊이로
    return


N = int(input())
odd_graph = [[] for _ in range(2*N-1)]
even_graph = [[] for _ in range(2*N-1)]
# 희소한 인접 리스트 방식
for r in range(N):
    for c, v in enumerate(list(map(int, input().split()))):
        if v == 1:
            if (r+c) % 2 == 0:
                newr, newc = (r-c)+N-1, r+c
                even_graph[newr].append(newc)
            else:
                newr, newc = (r-c)+N-1, r+c
                odd_graph[newr].append(newc)


total_ans = 0

ans = 0
visited_c = [False for _ in range(2*N-1)]
dfs(r=0, local_ans=0, graph=odd_graph)
total_ans += ans

ans = 0
visited_c = [False for _ in range(2*N-1)]
dfs(r=0, local_ans=0, graph=even_graph)
total_ans += ans


print(total_ans)
