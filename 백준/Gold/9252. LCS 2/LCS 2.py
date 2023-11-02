a, b = input(), input()


dp = [[0 for _ in range(len(b)+1)]
      for _ in range(len(a)+1)]


for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j = len(a), len(b)
ans_arr = []
while i != 0 and j != 0:
    if a[i-1] == b[j-1]:
        ans_arr.append(a[i-1])
        i, j = i-1, j-1
    elif dp[i][j] == dp[i-1][j]:
        i = i-1
    elif dp[i][j] == dp[i][j-1]:
        j = j-1
    else:
        raise Exception
    

print(dp[-1][-1])
print(''.join(ans_arr)[::-1])
