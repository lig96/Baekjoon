N, M = map(int, input().split())
bytes = list(map(int, input().split()))
costs = list(map(int, input().split()))


dp = [[0 for _ in range(max(costs)*N+1)] for _ in range(N+1)]
# dp[i][cost] =
# app을 i개 내(0이라면 아예 안 씀)에서 cost를 내며 껐을 때
# 확보한 bytes의 최대값
#
# 인덱싱 여분을 만들기 위해 N+1,
# 최대 cost가 0이어도 행렬을 만들 수 있도록 max(costs)*N+1


for i in range(len(bytes)):
    cost = costs[i]
    byte = bytes[i]

    for col in range(0, cost):
        dp[i+1][col] = dp[i][col]  # i+1을 쓰지 않고 그대로
    for col in range(cost, len(dp[0])):
        dp[i+1][col] = max(
            dp[i][col-cost]+byte,  # i+1을 쓰고 byte를 더함
            dp[i][col]  # i+1을 쓰지 않고 그대로
        )


for i, v in enumerate(dp[-1]):
    if v >= M:
        print(i)
        break
