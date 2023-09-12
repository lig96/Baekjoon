# 2차원
# https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-9251-LCS-%ED%8C%8C%EC%9D%B4%EC%8D%AC


a1 = input()
a2 = input()


dp = [[0 for _ in range(len(a2)+1)] for _ in range(len(a1)+1)]
for i in range(1, len(a1)+1):
    for j in range(1, len(a2)+1):
        if a1[i-1] == a2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])
