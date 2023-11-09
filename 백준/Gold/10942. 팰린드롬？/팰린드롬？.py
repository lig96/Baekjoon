import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
SE = [list(map(int, input().split())) for _ in range(M)]


dp = [['-1' for _ in range(N+1)] for _ in range(N+1)]
# dp[s][e] = arr[s-1:e]가 팰린드롬이냐 아니냐
for length in range(0, 1):  # length가 0, 길이가 1
    for s in range(1, N+1-length):
        e = s+length
        dp[s][e] = '1'
for length in range(1, 2):  # length가 1, 길이가 2
    for s in range(1, N+1-length):
        e = s+length
        if arr[s-1] == arr[e-1]:
            dp[s][e] = '1'
        else:
            dp[s][e] = '0'
for length in range(2, N+1):  # length가 2, 길이가 3 이상
    for s in range(1, N+1-length):
        e = s+length
        if arr[s-1] == arr[e-1] and dp[s+1][e-1] == '1':
            dp[s][e] = '1'
        else:
            dp[s][e] = '0'


for S, E in SE:
    sys.stdout.write(dp[S][E]+'\n')
