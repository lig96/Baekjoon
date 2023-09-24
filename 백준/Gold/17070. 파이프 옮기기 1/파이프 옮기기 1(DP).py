# DP


N = int(input())
mat = []
mat.append([0 for row in range(N+1)])
for _ in range(N):
    temp = [0] + list(map(int, input().split()))
    mat.append(temp)


dp = [[[0 for d in range(3)] for r in range(N+1)] for c in range(N+1)]
# 인덱스를 1부터 시작하기 위해 변형
# dp[row][col][direction] 꼴

dp[1][2][0] = 1
# 초기값 1
for r in range(1, N+1):
    for c in range(1, N+1):
        if r == 1 and c == 2:
            continue
            # 초기값 1이 덮어씌워지는 것 방지
        if mat[r][c] == 0:
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
            # 가로 파이프 = 가로->가로 + 대각선->가로
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
            # 세로 파이프
        if mat[r][c] == mat[r-1][c] == mat[r][c-1] == 0:
            dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]
            # 대각선 파이프


print(sum(dp[-1][-1]))
