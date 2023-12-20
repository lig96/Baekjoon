# prev * 8*8행렬 = now_1
# ................ prev * 8*8행렬 = now_2
# 계속 prev, now를 스왑하며 8*8행렬을 오른쪽에 곱함
# 결국 아래와 동일함
# [1, 0, 0, 0, 0, 0, 0, 0] * (8*8행렬)D제곱 = now_D
# 알고리즘 : 분할 정복을 이용한 거듭제곱


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
    assert len(left[0]) == len(right)
    R = len(left)
    C = len(right[0])
    K = len(left[0])  # len(right)

    temp = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            for k in range(K):
                temp[r][c] += left[r][k]*right[k][c]
                temp[r][c] %= mod

    return temp


D = int(input())
mod = 1_000_000_007
graph = [[0 for _ in range(8)] for _ in range(8)]
for s, e in [(0, 1), (0, 3), (1, 2), (1, 3),
             (2, 3), (2, 4), (2, 5), (3, 5),
             (4, 5), (4, 6), (5, 7), (6, 7)]:
    graph[s][e] = 1
    graph[e][s] = 1
#                             전산관1 정보과학관0
#           신양관2
#     진리4                    미래3
# 학생6                    한경직5
#                     형남7


prev = [[1, 0, 0, 0, 0, 0, 0, 0]]  # 이차원인 것 유의
graph = do_power(graph, D)


ans = do_matmul(prev, graph)


print(ans[0][0])
