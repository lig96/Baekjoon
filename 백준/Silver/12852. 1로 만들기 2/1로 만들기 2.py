from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write


def print_answer():
    print(str(dp[1])+'\n')

    ans = deque()
    now = 1
    while True:
        ans.appendleft(str(now))
        if now != parent[now]:
            now = parent[now]
        else:
            break
    print(' '.join(ans))
    return


N = int(input())


dp = [int(1e7) for _ in range(N+1)]
dp[N] = 0
parent = [i for i in range(N+1)]


for ind in range(N, -1, -1):
    if ind % 3 == 0:
        if dp[ind//3] > dp[ind]+1:
            dp[ind//3] = dp[ind]+1
            parent[ind//3] = ind

    if ind % 2 == 0:
        if dp[ind//2] > dp[ind]+1:
            dp[ind//2] = dp[ind]+1
            parent[ind//2] = ind

    if True and (ind-1) >= 0:
        if dp[ind-1] > dp[ind]+1:
            dp[ind-1] = dp[ind]+1
            parent[ind-1] = ind


print_answer()
