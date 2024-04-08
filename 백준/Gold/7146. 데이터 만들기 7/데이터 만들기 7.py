# 공통 조건
# 70 < V < 1000
# 제로 인덱싱
# 1500 < E < 1_000_000
# 셀프루프 없음. 중복간선 없음.
# 무방향

# https://www.acmicpc.net/problem/7146
# 데이터 만들기 7
# A = 도박1. 시간 초과 X
# B = 재귀백트래킹. 시간 초과
# T = 3004


def RecursiveBacktracking():
    def backtrack(u, label):
        nonlocal counter, found, ans

        if found:
            return

        counter += 1
        cur[u] = label  # assign label to u
        if u == V-1:
            found = True
            ans = cur[::]
            return

        # explore neighbors
        ok = [True for _ in range(X)]

        for j in range(len(AdjList[u+1])):
            counter += 1
            if counter > 1000000:
                return

            v = AdjList[u+1][j]
            if cur[v] != -1:
                ok[cur[v]] = False

        for j in range(X):
            if ok[j]:
                backtrack(u+1, j)
        return

    INF = 1_000_000_000
    ans = []

    V, E = map(int, input().split())
    AdjList = [[] for _ in range(V)]
    for i in range(E):
        a, b = map(int, input().split())
        AdjList[a].append(b)
        AdjList[b].append(a)

    found = False
    counter = 0
    for X in range(2, V+1):
        cur = [-1 for _ in range(V)]
        backtrack(0, 0)
        if found:
            break

        if counter > 1_000_000:
            print("TLE")
            return 1

    print(X)
    print(' '.join(map(str, ans)))
    print(f"The value of counter is: {counter}")
    return 0


MODE = ['for_bj_submission', 'for_local_verification'
        ][0]

if MODE == 'for_bj_submission':
    T = 3004  # (2+2E) = 3004
    TARGET = 1_000_000  #

    V = 71  # 70 < V < 1000
    E = 1501  # 1501로 고정

    adj_mat = [[False for _ in range(V)] for _ in range(V)]
    used_edges = 0
    for s in range(V):
        for e in range(s+1, V):
            if used_edges != E:
                adj_mat[s][e] = True
                adj_mat[e][s] = True
                used_edges += 1
    # 최대한 완전그래프가 되게끔.

    print(f'{V} {E}')
    for s in range(V):
        for e in range(s+1, V):
            if adj_mat[s][e]:
                print(f'{s} {e}')
elif MODE == 'for_local_verification':
    # RecursiveBacktracking()
    pass
