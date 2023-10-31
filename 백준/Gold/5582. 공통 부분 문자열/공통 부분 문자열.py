a = input()  # ab
b = input()  # defgh


dp = [0 for _ in range(len(b)+1)]
ans = 0
#   0 d e f g h
# 현재
# 공간복잡도 N. 뒤에서부터 인덱싱.


for r in range(1, len(a)+1):
    a_temp = a[r-1]
    for c in range(len(b), 0, -1):
        if a_temp == b[c-1]:
            dp[c] = dp[c-1]+1
            if dp[c] > ans:
                ans = dp[c]
        else:
            dp[c] = 0


print(ans)
