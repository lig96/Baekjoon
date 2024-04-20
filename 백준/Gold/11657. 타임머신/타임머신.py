import sys
input = sys.stdin.readline


def bellman_ford(S):
    dist = [INF for _ in range(N+1)]
    dist[S] = 0

    for _ in range(N-1):
        for start, nxt, cost in edges:
            # if dist[start] == INF:
            #     # 진짜 무한이라 필요없음.
            #     continue
            temp = dist[start] + cost
            if dist[nxt] > temp:
                dist[nxt] = temp
    else:
        flag = False
        for start, nxt, cost in edges:
            temp = dist[start] + cost
            if dist[nxt] > temp:
                flag = True
    return flag, dist


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]


INF = float('INF')


is_negative_cycle, dist = bellman_ford(1)


if is_negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        print(dist[i] if dist[i] != INF else -1)
