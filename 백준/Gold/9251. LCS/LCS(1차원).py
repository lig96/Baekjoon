# 1차원
# https://myjamong.tistory.com/317


a1 = input()
a2 = input()


dp = [0 for _ in range(len(a2))]
for i in range(len(a1)):
    cnt = 0
    for j in range(len(a2)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif (cnt >= dp[j]) and (a1[i] == a2[j]):
            dp[j] = cnt+1
        # elif (cnt >= dp[j]) and (a1[i] != a2[j]):
        #     dp[j] = dp[j]


print(max(dp))
