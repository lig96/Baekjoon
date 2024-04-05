# 공통 조건
# 0 < V <= 300
# 정점은 제로 인덱싱
# abs(w) < 1e6
# 0 <= 간선 <= 5_000
# 0 < Q <= 10
# 음수 사이클 불가능

# https://www.acmicpc.net/problem/7141
# 데이터 만들기 2
# A = 플로이드워셜. 시간 초과 X
# B = 최적화벨만포드. 시간 초과
# T = 2222


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
    T = 2222  # (1+V+2E) + (1+2Q) = 2222
    TARGET = 1_000_000  # Q*(V-1)*E = 1_039_500

    V = 100  # V > 100이면 플로이드워셜이 터짐. 클수록 좋음.
    E = 1_050  # 클수록 좋음.
    Q = 10  # 클수록 좋음

    adj_mat = [[None for _ in range(V)] for _ in range(V)]
    for s in range(V):
        e = s-1
        if E:
            adj_mat[s][e] = 1  # w=1로 고정. 이걸로 change 플래그 갱신.
            E -= 1
    for s in range(V):
        for e in range(V):
            if s == e:
                continue
            if E and adj_mat[s][e] is None:
                adj_mat[s][e] = 123_456  # w를 큰 값으로 고정
                E -= 1
    # _XX1
    # 2_XX
    # X3_X
    # XX4_
    # 형태.
    #
    # i = 0일 때, 1을 이용해 0->3 갱신. 4를 이용해 0->3->2 갱신.
    # i = 1일 때, 3을 이용해 0->2->1 갱신.
    # i = 2일 때, 갱신 없음.
    #
    # 엄밀히 말하면 i = 0일 때, X로 인하여 모든 거리가 갱신됨.
    # 또한 2는 필요없음. 자기 자신의 거리는 언제나 0이니까.

    print(V)
    for s in range(V):
        edges = [(i, v) for (i, v) in enumerate(adj_mat[s])
                 if v is not None]
        print(len(edges), end=' ')
        print(' '.join(map(lambda x: ' '.join(map(str, x)), edges)))
    print(Q)
    for _ in range(Q):
        print('0 1')
elif MODE == 'for_local_verification':
    # ModifiedDijkstra()
    # FloydWarshall()
    # OptimizedBellmanFord()
    pass
