import itertools
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(5e5))


def permutations(arr, r):
    def _permutation(arr, r, used, ret):
        if len(ret) == r:
            yield ret
        else:
            for i in range(len(arr)):
                if not used[i]:
                    ret.append(arr[i])
                    used[i] = True
                    yield from _permutation(arr, r, used, ret)
                    ret.pop()
                    used[i] = False
    yield from _permutation(arr, r, [False for _ in range(N)], [])


def sol(arr):
    global ans

    temp = -INF
    for i in range(len(arr)):
        start = arr[i]
        end = arr[(i+1) % len(arr)]  # 맨 끝 -> 맨 처음도 고려
        cost = adj_graph[start][end]
        temp = max(temp, cost)
        if temp >= ans[0]:
            break
    else:
        if ans[0] > temp:
            ans = [temp, arr[:]]
    return


INF = float('inf')
N, M = map(int, input().split())
adj_graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    adj_graph[u][v] = c


ans = [INF, []]
for permu in itertools.permutations(range(1, N+1), N):
    # P(9, 9) = 9! = 362_880
    sol(permu)


if ans[0] == INF:
    print(-1)
else:
    print(ans[0])
    print(*ans[1])
