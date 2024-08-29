import sys
input = sys.stdin.readline


N = int(input())
events = [list(map(int, input().split())) for _ in range(N)]
events.sort(key=lambda x: x[0])


INF = float('inf')  # 도달 불가능 혹은 BANG의 대상이 되는 시간
dp = [[INF for _ in range(2001)] for _ in range(N+1)]
# dp[i][loc] = d,
# i(원인덱싱)번째 이벤트 상황에서 loc에 도달하는 최소 이동거리
# -1000 ~ 0 ~ 1000 -> 2001개
# 쉬프트해서
# 0 ~ 1000 ~ 2000 -> 2001개로 변경
dp[0][1000] = 0


for i, (T, A, B) in enumerate(events):
    available_time = T - events[i-1][0] if i != 0 else T
    A += 1000
    B += 1000
    i += 1  # 원인덱싱

    for loc in range(2001):
        if dp[i-1][loc] == INF:
            continue
        for nxt in range(available_time+1):
            if 0 <= loc+nxt < 2001:
                dp[i][loc+nxt] = min(dp[i-1][loc] + nxt,
                                     # dp[i-1][loc+nxt],
                                     # # nxt == 0이면 윗 항과 동일
                                     dp[i][loc+nxt])
            if 0 <= loc-nxt < 2001:
                dp[i][loc-nxt] = min(dp[i-1][loc] + nxt,
                                     # dp[i-1][loc-nxt],
                                     # # nxt == 0이면 윗 항과 동일
                                     dp[i][loc-nxt])

    for loc in range(A+1, B):
        dp[i][loc] = INF


ans = min(dp[-1])
print(-1 if ans == INF else ans)
