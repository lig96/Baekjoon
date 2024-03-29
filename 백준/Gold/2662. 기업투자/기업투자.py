# 냅색 + 효율적인 역추적
#
# 공간복잡도(와 시간복잡도)가 나쁘지만 편하게 구현하려면
# how_much[사용한기업][사용한금액] =
# 최대이익을 만드는 [기업i에 투자한 금액들]
# 을 구현 후 how_much[-1][max_i]를 출력하면 됨


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
table = []
table.append([0 for _ in range(M)])  # 투자금액 0
for _ in range(N):
    _, *temp = map(int, input().split())
    table.append(temp)  # 투자금액 1, ~~~, N
# table[투자금액][기업] = 이익


bag = [[0 for _ in range(N+1)] for _ in range(M)]
# bag[사용한기업][사용한금액] = 최대이익
how_much = [[[0, 0, 0] for _ in range(N+1)] for _ in range(M)]
# how_much[사용한기업][사용한금액] =
# 최대이익을 만드는 [직전 사용한기업, 직전 사용한금액, 지금 추가된 금액]
for inv in range(0, N+1):
    bag[0][inv] = table[inv][0]
    how_much[0][inv] = [0, 0, inv]
# 기업 0의 초기값


for comp in range(1, M):
    for inv in range(N+1):
        for x in range(0, inv+1):
            temp = bag[comp-1][x]+table[inv-x][comp]
            if bag[comp][inv] < temp:
                bag[comp][inv] = temp
                how_much[comp][inv] = [comp-1, x, inv-x]


max_v = -1
max_i = None
for i, v in enumerate(bag[-1]):
    if max_v < v:
        max_v = v
        max_i = i
print(max_v)
x, y, z = -1, max_i, None
stack = []
for _ in range(M):
    x, y, z = how_much[x][y]
    stack.append(z)
print(*stack[::-1])
