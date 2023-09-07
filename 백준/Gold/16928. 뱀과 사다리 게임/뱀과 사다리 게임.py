from collections import deque


N, M = map(int, input().split())
ladders = {int(x): int(y) for x, y in
           (input().split() for _ in range(N))}
snakes = {int(u): int(v) for u, v in
          (input().split() for _ in range(M))}
cnt = [int(1e9) for _ in range(100+1)]
visited = [False for _ in range(100+1)]
qu = deque()


def bfs(v):
    cnt[v] = 0
    visited[v] = True
    qu.append(v)

    while qu:
        now = qu.popleft()
        if now == 100:
            print(cnt[100])
            return
        for dice in [1, 2, 3, 4, 5, 6]:
            after = now + dice
            if (after <= 100) and (not visited[after]):
                if after in ladders.keys():
                    after = ladders[after]
                elif after in snakes.keys():
                    after = snakes[after]
                else:
                    after = after
                if not visited[after]:
                    visited[after] = True
                    cnt[after] = cnt[now] + 1
                    qu.append(after)


bfs(1)