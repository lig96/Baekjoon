# 방법 1: 브루트포스
# 방법 2: DP


import sys
input = sys.stdin.readline


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]


dp = [0 for _ in range(N+1)]
# dp[nxt] = (i까지의 일정표를 사용했고) 다음 이용 가능한 상담 날짜가 nxt일 때 금액의 최댓값
# nxt는 0...N까지 총 N+1개여야 한다. 퇴사 당일에 이용이 가능하다는 것은 퇴사 전날에 이용이 끝났다는 의미이다.


for i in range(N):
    if i+table[i][0] < N+1:
        dp[i+table[i][0]] = max(
            max(dp[x] for x in range(i+1)) + table[i][1],
            dp[i+table[i][0]]
        )


print(max(dp))
