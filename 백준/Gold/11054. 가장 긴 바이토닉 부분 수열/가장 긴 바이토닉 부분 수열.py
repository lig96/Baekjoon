N = int(input())
A = list(map(int, input().split()))

dp_in = [1 for _ in range(N)]
# dp[i] = A[i]가 마지막일 때 증가 조건을 만족하는 수열의 최대 길이
dp_de = [1 for _ in range(N)]
# dp[i] = A[i]가 처음일 때 감소 조건을 만족하는 수열의 최대 길이


for i in range(N):
    for prev in range(i):
        if A[i] > A[prev]:
            if dp_in[prev]+1 > dp_in[i]:
                dp_in[i] = dp_in[prev]+1
        if A[-i-1] > A[-prev-1]:
            if dp_de[-prev-1]+1 > dp_de[-i-1]:
                dp_de[-i-1] = dp_de[-prev-1]+1


print(max([dp_in[i]+dp_de[i] for i in range(N)])-1)
