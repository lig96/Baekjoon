# 공통 조건
# 0 < V <= 300
# 정점은 제로 인덱싱
# abs(w) < 1e6
# 0 <= 간선 <= 5_000
# 0 < Q <= 10
# 음수 사이클 불가능

# https://www.acmicpc.net/problem/7143
# 데이터 만들기 4
# A = 플로이드워셜. 시간 초과 X
# B = 다익스트라. 시간 초과
# T = 157


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
    T = 157  # (1+V+2E) + (1+2Q) = 157
    TARGET = 1_000_000
    # V를 더 늘리면 T 제한을 위배
    # 39, 57, 1일 때 counter=1_572_862, T=157 -> Q=1일 때 TLE, 157
    # 37, 54, 1일 때 counter=  786_420, T=149
    # 35, 51, 1일 때 counter=  393_214, T=141
    # 33, 48, 1일 때 counter=  196_606, T=133 -> Q=6일 때 TLE, 143
    # V를 더 줄이면 TLE 조건을 위배
    # 31, 45, 1일 때 counter=   98_302, T=125

    V = 39
    E = 57
    Q = 1
    # print(f'T is {(1+V+2*E)+(1+2*Q)}')

    adj_mat = [[None for _ in range(V)] for _ in range(V)]
    used_E = 0
    left_down, middle_up, right_down = 1, 2, 0
    pos_w, neg_w = 1, -2
    while used_E < E:
        adj_mat[left_down][right_down] = 0
        adj_mat[left_down][middle_up] = pos_w
        adj_mat[middle_up][right_down] = neg_w
        used_E += 3
        left_down, middle_up, right_down = (
            left_down+2, middle_up+2, left_down
        )
        pos_w, neg_w = pos_w*2, neg_w*2
        # assert E % 3 == 0
        # assert abs(pos_w) < int(1e6)
        # assert abs(neg_w) < int(1e6)
    #     4        2
    #  (2) (-4) (1) (-2)
    # 3  (0)   1  (0)  0
    # 형태.

    print(V)
    for s in range(V):
        edges = [(i, v) for (i, v) in enumerate(adj_mat[s])
                 if v is not None]
        print(len(edges), end=' ')
        print(' '.join(map(lambda x: ' '.join(map(str, x)), edges)))
    print(Q)
    for _ in range(Q):
        print(f'{V-2} {0}')
elif MODE == 'for_local_verification':
    # ModifiedDijkstra()
    # FloydWarshall()
    # OptimizedBellmanFord()
    pass
