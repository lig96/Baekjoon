from collections import deque


def bfs(start):
    global ans_depth, ans_methods

    visited = [0 for _ in range(100_000+1)]
    visited[start] = 0
    qu = deque()
    qu.append((start, 0))

    while qu:
        now, now_depth = qu.popleft()

        if now == K:
            ans_depth = now_depth
            ans_methods += 1
            # 라인 A 때문에
            # visited[now=K]는 언제나 최단 경로이고
            # qu 속의 인자는 (위치, 최단 경로)로만 들어옴.
            # (K, 최단 경로보다 긺)을 걱정할 필요 없음.
            continue

        if (ans_depth != 'default') and (now_depth-1 == ans_depth):
            return

        for newx in [now-1, now+1, now*2]:
            if 0 <= newx <= 100_000:
                if (visited[newx] == 0) or (visited[newx] == now_depth+1):
                    # 방문한 적 없을 때 or 방문한 적 있지만 최단경로==현재경로일 때
                    #
                    # 최단 경로보다 현재 경로가 멀리 돌아왔다면 no. 라인 A.
                    # 최단 경로보다 작은 것은 애초에 없음
                    # bfs 특성상 visited[i]는 언제나 최단 경로
                    visited[newx] = now_depth+1
                    qu.append((newx, now_depth+1))


N, K = map(int, input().split())


if K <= N:
    print(N-K)
    print(1)
    exit()
else:
    ans_depth, ans_methods = 'default', 0
    bfs(N)
    print(ans_depth)
    print(ans_methods)
