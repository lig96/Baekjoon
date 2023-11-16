# dp[s][e] = min(
#     dp[s][i] + dp[i][e] + 결과물 간의 행렬 연산
# )

# ABCD - dp[0][3]
# = min(
# A, BCD - dp[0][0], dp[1][3], 왼쪽결과물*오른쪽결과물 행렬 연산
# AB, CD - dp[0][1], dp[2][3], 왼쪽결과물*오른쪽결과물 행렬 연산
# ABC, D - dp[0][2], dp[3][3], 왼쪽결과물*오른쪽결과물 행렬 연산
# )

# ((AB)C)D - ABC_D좌
# (AB)(CD) - AB_CD
# (A(BC))D - ABC_D우
# A((BC)D) - A_BCD좌
# (AB)(CD) - AB_CD
# A(B(CD)) - A_BCD우


N = int(input())
rcs = [tuple(map(int, input().split())) for _ in range(N)]


dp = [[float('INF') for _ in range(N)] for _ in range(N)]
# dp[s][e]
# s, ~, e 인덱스를 사용한 여러 행렬 곱셈의 최소 연산 횟수


for i in range(N):
    dp[i][i] = 0
    # 1개만을 사용한다면 연산은 0
for gap in range(1, N):
    for s in range(0, N-gap):
        e = s+gap
        # 반복문을 사용한 방법
        for i in range(s, e):
            temp1 = dp[s][i] + dp[i+1][e]
            temp2 = rcs[s][0] * rcs[i][1] * rcs[e][1]
            temp = temp1 + temp2
            if dp[s][e] > temp:
                dp[s][e] = temp
        # 리스트 컴프리헨션을 사용한 방법
        # dp[s][e] = min(
        #     [dp[s][i] + dp[i+1][e] + rcs[s][0]*rcs[i][1]*rcs[e][1]
        #      for i in range(s, e)]
        # )


print(dp[0][N-1])
