# DP


N = int(input())
mat = []
mat.append([0 for row in range(N+1)])
for _ in range(N):
    temp = [0] + list(map(int, input().split()))
    mat.append(temp)


dp = [[[0 for dir in range(3)]
       for col in range(N+1)] for row in range(N+1)]
# 인덱스를 1부터 맞춰주기 위해 1씩 추가.


dp[1][2][0] = 1
for r in range(1, N+1):
    for c in range(1, N+1):
        if r == 1 and c == 2:
            # 초기값 1이 덮어씌워지는 것 방지
            continue
        if mat[r][c] == 0:
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
        if mat[r][c] == mat[r-1][c] == mat[r][c-1] == 0:
            dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]


print(sum(dp[-1][-1]))
# 0 가로
# 1 세로
# 2 대각선