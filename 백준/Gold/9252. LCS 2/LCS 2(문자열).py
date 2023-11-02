a, b = input(), input()


dp = [['' for _ in range(len(b)+1)]
      for _ in range(len(a)+1)]


for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + a[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            elif len(dp[i-1][j]) < len(dp[i][j-1]):
                dp[i][j] = dp[i][j-1]


print(len(dp[-1][-1]))
print(dp[-1][-1])
# 답이 0, ''일 경우 print('')은 공백 처리되어서 채점에서 허용
    
