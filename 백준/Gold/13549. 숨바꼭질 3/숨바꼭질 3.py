from collections import deque


N, K = map(int, input().split())


MAX_K = min(2*K+1, 100_000+1) if N < K else (print(N-K), exit())
visited = [-1 for _ in range(MAX_K)]
visited[N] = 0
qu = deque([(N, 0)])

while qu:
    loc, time = qu.popleft()

    for newloc, newtime in zip((loc*2, loc-1, loc+1), (time, time+1, time+1)):
        if (0 <= newloc < len(visited)) and (visited[newloc] == -1):
            visited[newloc] = newtime
            qu.append((newloc, newtime))
    # 4-5-6이 아닌 4-3-6이 되어야 하기 때문에
    # -가 +보다 먼저 와야 한다.
    if visited[K] != -1:
        break


print(visited[K])