# MODE = 0
# Python3 524ms, PyPy3 252ms
# 친구가 필요한 구간, 아닌 구간으로 나눔
# dp[0][0] = 0번째 구간에서 0 이하인 원소의 개수
# dp[i][k] = 0..i번째 구간을 쓰고 그 구간에서 총 k명을 쓸 때 최대 시간
#          = max(i번째구간에서now이하인원소의개수 + dp[i-1][k-now])
#            단 now는 i번째 구간에서 쓰는 인원, k-now은 0..i-1번째 구간에서 쓰는 인원
#
# MODE = 1
# Python3 시간 초과, PyPy3 3036ms
# 구간 나누지 않고 전체 time을 순회하고 0을 만나는 순간 분기
# dp[time][now][left] = time 시점에서 now를 쓰고
#                       과거 사용, 현재 사용 빼고 left가 남았을 때 최대 시간
#                     = 점화식[
#                       dp[t][0][left] = dp[t-1][0][left]
#                       dp[t][now][left] = dp[t-1][0][now + left]
#                       dp[t][0][left] = max(
#                           dp[t-1][temp_now][left] for temp_now in range(K+1))
#                       dp[t][now][left] = dp[t-1][now][left]
#                       ] 중 하나
#                       추가로 dp[t][now][left] += int(needed[t] <= now)


MODE = 0
if MODE == 0:
    # 라이브러리
    import sys
    input = sys.stdin.readline

    # 입력 받기
    N, M, K, T = map(int, input().split())
    believers = [list(map(int, input().split())) for _ in range(M)]

    # imos 효율적인 구간 합
    needed = [0 for _ in range(N+1)]
    for s, e in believers:
        needed[s] += 1
        if e < N+1:
            needed[e] -= 1
    temp = 0
    for i in range(len(needed)):
        temp += needed[i]
        needed[i] = max(T-temp, 0)
    needed[0] = 0
    # print(needed)
    # [0, 2, 2, 1, 1, 0, 0, 0, 0, 0, 1, 1]

    # 파티션 만들기
    partitions = []
    temp = []
    temp_type = None
    for needed_v in needed:
        if needed_v == 0:
            if temp_type == 'zero':
                temp.append(needed_v)
            else:
                temp_type = 'zero'
                partitions.append(temp)
                temp = []
                temp.append(needed_v)
        else:
            if temp_type == 'pos':
                temp.append(needed_v)
            else:
                temp_type = 'pos'
                partitions.append(temp)
                temp = []
                temp.append(needed_v)
    else:
        # 맨 마지막 temp는 처리가 안 되었음
        partitions.append(temp)
    # print(partitions)
    # [[0], [2, 2, 1, 1], [0, 0, 0, 0, 0], [1, 1]]

    # 파티션 내에서 특정 값 이하인 원소들 세기
    part_counts = [[0 for _ in range(300+1)] for _ in range(len(partitions))]
    for i in range(len(partitions)):
        for v in partitions[i]:
            part_counts[i][v] += 1
        for j in range(1, 300+1):
            part_counts[i][j] += part_counts[i][j-1]
    # part_counts[part_i][x] = len(v for v in partitions[part_i] if v<=x)
    # i번째 파티션에 친구 v명을 투입하면 얻을 수 있는 강림 시간의 양

    # dp 만들기
    # dp[0][0] = 0번째 구간에서 0 이하인 원소의 개수
    # dp[i][k] = 0..i번째 구간을 쓰고 그 구간에서 총 k명을 쓸 때 최대 시간
    #          = max(i번째구간에서now이하인원소의개수 + dp[i-1][k-now])
    #            단 now는 i번째 구간에서 쓰는 인원, k-now은 0..i-1번째 구간에서 쓰는 인원
    dp = [[-float('inf') for _ in range(K+1)] for _ in range(len(partitions))]
    for part_i in [0]:
        # 첫 구간은 needed가 0인 게 고정이고
        # 그 구간에서는 과거친구0, 현재친구가 0명이니 총친구도 0명인 게 고정
        dp[part_i][0] = part_counts[part_i][0]
    # 초기값

    # dp 돌리기
    for part_i in range(1, len(partitions)):
        for k in range(K+1):
            if partitions[part_i][0] == 0:
                # now=0으로 고정
                dp[part_i][k] = part_counts[part_i][0]+dp[part_i-1][k]
            else:
                dp[part_i][k] = max(
                    part_counts[part_i][now]+dp[part_i-1][k-now] for now in range(k+1)
                )

    # 정답 출력하기
    print(max(dp[-1])-1)  # 0시~1시는 해당이 안 돼서 1 빼줘야 함

elif MODE == 1:
    # 라이브러리
    import sys
    input = sys.stdin.readline

    # 입력 받기
    N, M, K, T = map(int, input().split())
    believers = [list(map(int, input().split())) for _ in range(M)]

    # imos 효율적인 구간 합
    needed = [0 for _ in range(N+1)]
    for s, e in believers:
        needed[s] += 1
        if e < N+1:
            needed[e] -= 1
    temp = 0
    for i in range(len(needed)):
        temp += needed[i]
        needed[i] = max(T-temp, 0)
    needed[0] = 0
    # print(needed)
    # [0, 2, 2, 1, 1, 0, 0, 0, 0, 0, 1, 1]

    # dp 만들기
    # dp[time][now][left] = time 시점에서 now를 쓰고
    #                       과거 사용, 현재 사용 빼고 left가 남았을 때 최대 시간
    #                     = 점화식[
    #                       dp[t][0][left] = dp[t-1][0][left]
    #                       dp[t][now][left] = dp[t-1][0][now + left]
    #                       dp[t][0][left] = max(
    #                           dp[t-1][temp_now][left] for temp_now in range(K+1))
    #                       dp[t][now][left] = dp[t-1][now][left]
    #                       ] 중 하나
    #                       추가로 dp[t][now][left] += int(needed[t] <= now)
    dp = [[[-float('inf') for _ in range(K+1)]
           for _ in range(K+1)]
          for _ in range(N+1)]
    dp[0][0][K] = 1  # needed[time=0]=0이라서 now=0이어도 1
    # 초기값

    # dp 돌리기
    for t in range(1, N+1):
        for now in range(0, K+1):
            for left in range(0, K+1):
                cond1 = (needed[t-1] == 0)
                cond2 = (needed[t] == 0)
                if cond1 and cond2:
                    # 0, 0
                    # now=0, now=0
                    if dp[t][0][left] == -float('inf'):
                        dp[t][0][left] = dp[t-1][0][left]
                    else:
                        # 이미 갱신이 됐으면 갱신 안 함
                        pass
                elif cond1 and not cond2:
                    # 0, 양수
                    # now=0, 모든 now
                    if now+left <= K:
                        dp[t][now][left] = dp[t-1][0][now + left]
                    else:
                        # 인덱스에러
                        pass
                elif not cond1 and cond2:
                    # 양수, 0
                    # 모든 now, now=0
                    if dp[t][0][left] == -float('inf'):
                        dp[t][0][left] = max(
                            dp[t-1][temp_now][left] for temp_now in range(K+1)
                        )
                    else:
                        # 이미 갱신이 됐으면 갱신 안 함
                        pass
                elif not cond1 and not cond2:
                    # 양수, 양수
                    # 모든 now, 모든 now
                    # t-1에 now였으면 t에 now보다 작은 값은 불가능함
                    # t에 now보다 큰 값은 가능한데 이럴 거면 애초에 t-1에 큰 값을 넣는 게 약우월이고
                    # 그러한 선택은 이미 (cond1 and not cond2)에서 분기됨
                    dp[t][now][left] = dp[t-1][now][left]
                else:
                    raise Exception
                dp[t][now][left] += int(needed[t] <= now)

    # 정답 출력하기
    print(max(map(max, dp[-1]))-1)
