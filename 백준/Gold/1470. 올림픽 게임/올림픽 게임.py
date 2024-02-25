def key(x):
    return (-x[0], -x[1], -x[2], x[3])


def check(s_use, max_b):
    '''
    medals[ans]와 medals[ans+1]이
    s_use 개만큼의 은메달과 b_use 개만큼의 동메달을 썼을 때
    순위가 뒤바뀔 수 있다면 가장 작은 양의 정수 b_use 를 리턴,
    없다면 None 리턴

    '''
    b_diff = max(0, medals[initial][2] - medals[rank+1][2])
    for b_use in range(b_diff, b_diff+2):
        if b_use > max_b:
            continue
        if b_use > (L-s_use):
            continue

        medals[rank+1][1] += s_use
        medals[rank+1][2] += b_use

        if key(medals[initial]) > key(medals[rank+1]):
            medals[rank+1][1] -= s_use
            medals[rank+1][2] -= b_use
            return b_use

        medals[rank+1][1] -= s_use
        medals[rank+1][2] -= b_use
    return None


N, L = map(int, input().split())
medals = [list(map(int, input().split()))+[i] for i in range(N)]
# 제로 인덱싱, 4번째 규칙은 팀 번호


medals[0][0] += L
# 1번 팀이 남은 L경기에서 모두 금메달
medals_0 = medals[0]
medals.sort(key=key)
initial = medals.index(medals_0)
# 정렬 후 초기 인덱스를 찾음
dp = [[-1 for _ in range(10_001)] for _ in range(N)]
# dp[rank][silver] = max_b
# 1번 팀이 rank까지 추락하고 silver만큼의 뿌려줄 여유가 있을 때
# 뿌려줄 여유가 있는 bronze의 최댓값
dp[initial][L] = L


for rank in range(initial, N-1):
    if medals[initial][0] > medals[rank+1][0]:
        # 애초에 금메달이 더 많아서
        # 은, 동을 어떻게 하든 순위를 못 바꾸는 경우
        break

    for silver in range(0, 10_001):
        if dp[rank][silver] == -1:
            continue

        s_diff = medals[initial][1] - medals[rank+1][1]
        b_diff = medals[initial][2] - medals[rank+1][2]

        # s를 딱 맞춰 쓰고 b를 더 쓰기
        if b_diff >= 0:
            if (s_diff + b_diff + 1) > L:
                pass
            elif silver-s_diff < 0:
                pass
            else:
                dp[rank+1][silver-s_diff] = max(
                    dp[rank+1][silver-s_diff], dp[rank][silver] - (b_diff+1))

        elif b_diff < 0:
            if s_diff > L:
                pass
            elif silver-s_diff < 0:
                pass
            else:
                dp[rank+1][silver-s_diff] = max(
                    dp[rank+1][silver-s_diff], dp[rank][silver])

        # s를 더 쓰기
        if (s_diff+1) > L:
            pass
        elif silver-(s_diff+1) < 0:
            pass
        else:
            dp[rank+1][silver-(s_diff+1)] = max(
                dp[rank+1][silver-(s_diff+1)], dp[rank][silver])


ans = -1
for rank in range(0, N):
    for silver in range(0, 10_001):
        if dp[rank][silver] != -1:
            ans = rank
print(ans+1)
# 제로 인덱싱이라 인덱스0이 등수1임


# for i in dp:
#     print(i[:10])
