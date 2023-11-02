import sys
# print(sys.getdefaultencoding())
# print(sys.stdin.encoding)
# print(sys.stdout.encoding)
# sys.stdin.reconfigure(encoding='utf-8')
# sys.stdout.reconfigure(encoding='utf-8')
# print(sys.getdefaultencoding())
# print(sys.stdin.encoding)
# print(sys.stdout.encoding)

if 'utf-8' != sys.stdin.encoding:
    raise Exception

a, b = input(), input()

dp = [[0 for _ in range(len(b)+1)]
      for _ in range(len(a)+1)]


for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])
