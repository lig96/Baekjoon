from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))


dp = deque(0 for _ in range(M))
# dp[i][n] = i를 사용하고 오른쪽 끝으로 하는 합이 n인
# 윈도우의 개수.
# 메모리 초과와 시간 초과 때문에 2차원 list 대신 1차원 deque로 선언하였다.
dp[arr[0] % M] += 1
ans = 0
ans += dp[0]


for i in range(1, N):
    # i-1을 사용하는 윈도우에 i를 덧붙이기
    dp.rotate(arr[i])
    # i 1개만 사용하기
    dp[arr[i] % M] += 1

    # 정답 갱신하기
    ans += dp[0]


print(ans)
