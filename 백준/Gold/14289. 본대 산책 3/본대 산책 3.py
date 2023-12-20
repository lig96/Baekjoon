# https://www.acmicpc.net/problem/12850
# 본대 산책2 참고

import sys
input = sys.stdin.readline


def do_power(graph, num):
    if num == 1:
        return graph

    if num % 2 == 0:
        # 2^100
        new = do_power(graph, num//2)
        # 2^50
        new = do_matmul(new, new)
        # 2^50 * 2^50 = 2^100
        return new
    else:
        # 2^101
        new = do_power(graph, num//2)
        # 2^50
        new = do_matmul(new, new)
        # 2^50 * 2^50 = 2^100
        new = do_matmul(new, graph)
        # 2^100 * 2^1 = 2^101
        return new


def do_matmul(left, right):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for k in range(n):
                temp[r][c] += left[r][k]*right[k][c]
                temp[r][c] %= mod
    return temp


n, m = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
D = int(input())
mod = 1_000_000_007


prev = [[1]+[0 for _ in range(n-1)]]  # 이차원인 것 유의
graph = do_power(graph, D)


ans = [[0 for _ in range(n)]]
for r in [0]:
    for c in range(n):
        for k in range(n):
            ans[r][c] += prev[r][k]*graph[k][c]


print(ans[0][0])
