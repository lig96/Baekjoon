import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))


def dfs1(x):
    if x == E:
        dp1[x] = True
        return

    visited[x] = True

    children = [nxt for nxt in graph[x] if not visited[nxt]]

    for child in children:
        dfs1(child)

    if any(dp1[child] for child in children):
        dp1[x] = True
    return


def dfs2(x, is_first_turn):
    if x == E:
        global ans
        ans = 'First'
        return

    visited[x] = True

    children = [nxt for nxt in graph[x] if not visited[nxt]]

    if is_first_turn:
        for child in children:
            if dp1[child]:
                # E를 포함한 경로
                dfs2(child, not is_first_turn)
    else:
        for child in children:
            if not dp1[child]:
                # E를 포함하지 않은 경로가 존재하면
                dfs2(child, not is_first_turn)
                break
        else:
            # break가 안 됐다는 건 E를 포함하지 않은 경로가 없다는 뜻
            dfs2(children[0], not is_first_turn)
    return


N, S, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


dp1 = [False for _ in range(N+1)]
# dp[i] = S가 루트인 트리에서 i 정점 아래로 갈 때 E를 함유하고 있는지 여부
visited = [False for _ in range(N+1)]
dfs1(S)  # S를 루트로 놓은 트리, dp 만드는 용


ans = 'Second'
visited = [False for _ in range(N+1)]
dfs2(S, True)
# 순회하며 최적 행동


print(ans)
