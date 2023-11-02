a, b = input(), input()


dp = [['' for _ in range(len(b)+1)]
      for _ in range(len(a)+1)]


for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + a[i-1]
        else:
            dp[i][j] = sorted([dp[i-1][j], dp[i][j-1]],
                              key=lambda x: -len(x))[0]

if dp[-1][-1]:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])
else:
    print(0)
