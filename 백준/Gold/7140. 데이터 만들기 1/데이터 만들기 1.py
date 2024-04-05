# 공통 조건
# 0 < V <= 300
# 정점은 제로 인덱싱
# abs(w) < 1e6
# 0 <= 간선 <= 5_000
# 0 < Q <= 10
# 음수 사이클 불가능

# https://www.acmicpc.net/problem/7140
# 데이터 만들기 1
# A = 다익스트라. 시간 초과 X
# B = 플로이드워셜. 시간 초과
# T = 107


def ModifiedDijkstra():
    from heapq import heappop, heappush

    INF = 1_000_000_000

    V = int(input())
    AdjList = [[] for _ in range(V)]
    for i in range(V):
        n, *a = map(int, input().split())
        for k in range(0, 2*n, 2):
            j, w = a[k], a[k+1]
            AdjList[i].append((j, w))

    counter = 0
    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        dist = [INF for _ in range(V)]
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            counter += 1
            if counter > 1_000_000:
                print("TLE because iteration counter > 1000000")
                return 1

            d, u = heappop(pq)
            if d == dist[u]:
                for j in range(0, len(AdjList[u])):
                    v = AdjList[u][j]
                    if dist[u] + v[1] < dist[v[0]]:
                        dist[v[0]] = dist[u] + v[1]
                        heappush(pq, (dist[v[0]], v[0]))

        print(dist[t])

    print(f"The value of counter is: {counter}")
    return 0


def FloydWarshall():
    V = int(input())
    M = [[1_000_000_000 for _ in range(V)] for _ in range(V)]
    for i in range(V):
        M[i][i] = 0

    for i in range(V):
        n, *a = map(int, input().split())
        for k in range(0, 2*n, 2):
            j, w = a[k], a[k+1]
            M[i][j] = min(M[i][j], w)

    counter = 0
    for k in range(V):
        for i in range(V):
            for j in range(V):
                counter += 1
                if counter > 1_000_000:
                    print("TLE because iteration counter > 1000000")
                    return 1
                M[i][j] = min(M[i][j], M[i][k] + M[k][j])

    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        print(M[s][t])

    print(f"The value of counter is: {counter}")
    return 0


def OptimizedBellmanFord():
    INF = 1_000_000_000

    V = int(input())
    AdjList = [[] for _ in range(V)]
    for i in range(V):
        n, *a = map(int, input().split())
        for k in range(0, 2*n, 2):
            j, w = a[k], a[k+1]
            AdjList[i].append((j, w))

    counter = 0
    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        dist = [INF for _ in range(V)]
        dist[s] = 0

        for i in range(V-1):
            change = False
            for u in range(V):
                for j in range(len(AdjList[u])):
                    counter += 1
                    if counter > 1_000_000:
                        print("TLE because iteration counter > 1000000")
                        return 1

                    v = AdjList[u][j]

                    if dist[u] + v[1] < dist[v[0]]:
                        dist[v[0]] = dist[u] + v[1]
                        change = True

            if not change:
                break

        print(dist[t])

    print(f"The value of counter is: {counter}")
    return 0


MODE = ['for_bj_submission', 'for_local_verification'
        ][0]

if MODE == 'for_bj_submission':
    # T = 107 # 조건 안 씀
    V = 101  # V > 100
    E = 0
    Q = 1

    adj_mat = [[None for _ in range(V)] for _ in range(V)]
    for s in range(V):
        for e in range(V):
            if s == e:
                continue
            if E:
                adj_mat[s][e] = 1  # w = 1로 고정
                E -= 1

    print(V)
    for s in range(V):
        edges = [(i, v) for (i, v) in enumerate(adj_mat[s])
                 if v is not None]
        print(len(edges), end=' ')
        print(' '.join(map(lambda x: ' '.join(map(str, x)), edges)))
    print(Q)
    print('0 1')
elif MODE == 'for_local_verification':
    # ModifiedDijkstra()
    # FloydWarshall()
    # OptimizedBellmanFord()
    pass
