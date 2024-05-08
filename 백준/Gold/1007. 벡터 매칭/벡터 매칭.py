# sum_vectors[0], 즉 벡터의 x좌표의 합은
# P(N, N)의 발상으로 한다면
# (0, 1), (2,3)일 때
# x_0 - x_1 + x_2 - x_3
# (2, 3), (0, 1)일 때는 이전과 동일함에도 중복으로 뽑히고
# 마찬가지로 x_0 - x_1 + x_2 - x_3
#
# 정리하면 (x_0+x_1+x_2+x_3) - 2*(x_1 + x_3)
# 쌍들의 순서 혹은 자신과 쌍을 이루는 다른 한 점의 좌표는 중요하지 않음.
#
# 한 쌍의 오른쪽에 오게 되는 점을 뽑는다의 발상으로 한다면
# (0, 1), (2, 3) -> 1, 3
# (2, 3), (0, 1) -> 1, 3
# C(N, N//2)로 됨.


import sys
input = sys.stdin.readline


def rec(start, depth):
    if depth == N//2:
        global min_ans

        sum_vectors = tot_sum_vectors[::]
        for x, y in right_points:
            sum_vectors[0] -= 2*x
            sum_vectors[1] -= 2*y

        temp = (sum_vectors[0]**2 + sum_vectors[1]**2)
        if min_ans > temp:
            min_ans = temp
        return

    for i in range(start, N+depth-N//2+1):
        right_points[depth] = points[i]
        # 매번 새로 갱신되니 초기화 안 해도 됨.
        rec(i+1, depth+1)
    return


T = int(input())
for _ in range(T):
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    min_ans = float('inf')
    right_points = [None for _ in range(N//2)]
    tot_sum_vectors = [sum(x for x, _ in points),
                       sum(y for _, y in points)]

    rec(0, 0)

    print(min_ans**0.5)
