x = int(input())
dp = [0 for _ in range(x+3)]
dp[1]=0
dp[2]=1
dp[3]=1

for i in range(4, x+1):
    temp = dp[i-1]
    if i%3==0:
        temp = min(temp, dp[i//3])
    if i%2==0:
        temp = min(temp, dp[i//2])
    dp[i] = temp + 1

print(dp[x])