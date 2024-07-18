import sys
input = sys.stdin.readline


N, M, K, T = map(int, input().split())
# 강림제 시작 1
# 강림제 끝 = 1+N = 12
believers = [list(map(int, input().split())) for _ in range(M)]


needed = [T for _ in range(N+1)]
for s, e in believers:
    for i in range(s, e):
        needed[i] = max(0, needed[i]-1)
needed[0] = 0
already_good_ans = needed.count(0) - 1  # 0시~1시는 충족이 안 된 거임
# [0, 2, 2, 1, 1, 0, 0, 0, 0, 0, 1, 1]

partitions = []
temp = []
for needed_v in needed:
    if needed_v == 0:
        partitions.append(temp)
        temp = []
    else:
        temp.append(needed_v)
else:
    # 맨 마지막 temp는 처리가 안 되었음
    partitions.append(temp)
partitions = [x for x in partitions if x]  # 빈 temp 거르기
# [[2, 2, 1, 1], [1, 1]]

part_counts = [[0 for _ in range(300+1)] for _ in range(len(partitions))]
for i in range(len(partitions)):
    for v in partitions[i]:
        part_counts[i][v] += 1
    for j in range(1, 300+1):
        part_counts[i][j] += part_counts[i][j-1]
# part_counts[part_i][x] = len(v for v in partitions[part_i] if v<=x)
# i번째 파티션에 친구 v명을 투입하면 얻을 수 있는 강림 시간의 양


# dp[0][k] = 0번째 구간에서 k이하인 원소의 개수
# dp[i][k] = 0..i번째 구간을 쓸 것이고 0..i번째 구간에서 총 k명의 친구를 쓸 것임
#           max(i번째구간에서now이하인원소의개수 + dp[i-1][0:k-now+1]의최댓값)
#           단 now는 i번째 구간에서 사용되는 인원, k-now+1은 0..i-1번째 구간에서 사용하는 인원
# (여기서 슬라이싱의 최댓값이 아니라 dp[i-1][k-now+1]만 해도 될 듯)
if len(partitions) == 0:
    print(already_good_ans)
    exit()

dp = [[0 for _ in range(K+1)] for _ in range(len(partitions))]
for part_i in [0]:
    for k in range(K+1):
        dp[part_i][k] = part_counts[part_i][k]
# 초기값

for part_i in range(1, len(partitions)):
    for k in range(K+1):
        dp[part_i][k] = max(
            part_counts[part_i][now]+dp[part_i-1][k-now]
            for now in range(k+1)
        )
        # (
        #     part_counts[part_i][now]+dp[part_i-1][k-now]
        #     for now in range(k+1)
        # )

print(max(dp[-1]) + already_good_ans)
