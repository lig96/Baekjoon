import sys
input = sys.stdin.readline


R, C = map(int, input().split())
mat = [list(map(int, list(input().rstrip()))) for _ in range(R)]


dp = [[0 for _ in range(C)] for _ in range(R)]
for r in range(R):
    dp[r][0] = 1 if mat[r][0] == 1 else 0
for c in range(C):
    dp[0][c] = 1 if mat[0][c] == 1 else 0
# (r, c)를 오른쪽 아래 꼭짓점으로 하는 정사각형의 최대 길이
# 자명히 좌변, 상변은 0 혹은 1이고 이게 dp의 초깃값
# 왼쪽 위 꼭짓점을 기준으로 삼는 게 발상은 편하나 반복문의 인덱스가 불편함


for r in range(1, R):
    for c in range(1, C):
        if mat[r][c] != 1:
            continue
        dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])+1


print(max(map(max, dp))**2)
