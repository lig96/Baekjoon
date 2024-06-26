# LIS 알고리즘
# O(N^2), O(NlogN)이 있는데
# O(NS)도 가능함.


import sys
input = sys.stdin.readline


N = int(input())
boxes = list(map(int, input().split()))


MODE = [0, 1][
    0]
if MODE == 0:  # O(NS)
    S = max(boxes)+1  # 최대 사이즈
    dp = [0 for _ in range(S)]
    # dp[size]
    # = i번째 박스까지 썼을 때
    # size 크기의 박스에 넣을 수 있는 최대 상자 개수
    for i in [0]:  # 초기값
        size = boxes[i]
        dp[size] = 1
    for i in range(1, N):
        size = boxes[i]
        dp[size] = max(dp[:size]) + 1
else:  # O(NN)
    dp = [1 for _ in range(N)]
    # dp[i]
    # = i번째 박스까지 썼을 때 최대 상자 개수
    # 초기값은 모두 1
    for i in range(N):
        for j in range(i):
            if boxes[j] < boxes[i]:
                dp[i] = max(dp[j]+1, dp[i])


print(max(dp))
