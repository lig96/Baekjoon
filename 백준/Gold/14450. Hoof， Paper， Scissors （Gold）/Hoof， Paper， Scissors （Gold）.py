import sys
input = sys.stdin.readline


def find_w_l_l_against(i):
    if i == 'S':
        return tuple(map(int, '012'))
    elif i == 'P':
        return tuple(map(int, '201'))
    else:
        return tuple(map(int, '120'))


N, K = map(int, input().split())
john_gestures = [input().rstrip() for _ in range(N)]
# 인덱싱은 H = 0, P = 1, S = 2


dp = [[-float('inf') for _ in range(K+1)] for _ in range(3)]
for i in range(3):
    dp[i][0] = 0
# dp[HPS][k] =
# n번째 농부 존의 제스처까지 왔고 n번째 때 사용한 베시의 제스처가 HPS이고
# k번 바꾸었을 때 최대 승리 수
#
# dp[승][k] = max(dp[승][k]+1,
#                dp[패1][k-1]+1,
#                dp[패2][k-1]+1)


for gesture in john_gestures:
    winner, loser1, loser2 = find_w_l_l_against(gesture)
    for k in range(0, 1):
        dp[winner][k] += 1
    for k in range(1, K+1):
        dp[winner][k] = max(dp[winner][k]+1,
                            dp[loser1][k-1]+1,
                            dp[loser2][k-1]+1)


print(max(map(max, dp)))
