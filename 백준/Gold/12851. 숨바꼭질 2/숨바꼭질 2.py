from collections import deque


def bfs(start):
    global ans_depth, ans_methods

    visited = [0 for _ in range(100_000+1)]
    visited[start] = 0
    qu = deque()
    qu.append(start)

    while qu:
        now = qu.popleft()

        if now == K:
            ans_depth = visited[now]
            ans_methods += 1
            # 라인 A 때문에 visited[now=K]는 언제나 최단 경로
            continue

        for newx in [now-1, now+1, now*2]:
            if 0 <= newx <= 100_000:
                if (visited[newx] == 0) or (visited[newx] == visited[now]+1):
                    # 방문한 적 없을 때 or 방문한 적 있지만 최단경로와 동일할 때
                    #
                    # 라인 A. 최단 경로보다 크게 돌아왔다면 no
                    # 최단 경로보다 작은 것은 애초에 없음
                    # bfs 특성상 visited[i]는 언제나 최단 경로
                    visited[newx] = visited[now]+1
                    qu.append(newx)


N, K = map(int, input().split())


if K <= N:
    print(N-K)
    print(1)
    exit()
else:
    ans_depth, ans_methods = 0, 0
    bfs(N)
    print(ans_depth)
    print(ans_methods)
