# 첫 번째 예시에서
# 은메달 3개를 주는 방법이 있고
# 은메달 2개, 동메달 4개를 주는 방법이 있는데
# 어느 방법이 최적 방법인지 명확하지 않다.
# 이럴 때 푸는 방법은 둘 다를 dp에 기록하면 된다.

# 함수화해서 반복되는 부분을 매개변수로 처리한다면
# 코드가 깔끔해지겠지만
# b_diff가 음수일 때 예외 처리를 떠올리기 어렵기 때문에
# 비슷한 문제를 만났을 때 어차피 그런 방식으로는 못 풀 것 같다.


N, L = map(int, input().split())
medals = [list(map(int, input().split()))+[i] for i in range(N)]
# 제로 인덱싱, 4번째 규칙은 팀 번호


medals[0][0] += L
# 1번 팀이 남은 L경기에서 모두 금메달
medals_0 = medals[0]
medals.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
initial = medals.index(medals_0)
# 정렬 후 초기 순위를 찾음
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

    for s in range(0, 10_001):
        if dp[rank][s] == -1:
            continue

        s_diff = medals[initial][1] - medals[rank+1][1]
        b_diff = medals[initial][2] - medals[rank+1][2]

        # s를 딱 맞춰 쓰고 b를 더 쓰기
        if b_diff >= 0:
            # 양수라면, 즉 동메달이 더 많아서 보충해야 한다면
            if (s_diff+b_diff+1) > L:
                # 한 경기에서 동시에 은, 동 메달을 얻을 수 없음
                pass
            elif (s-s_diff) < 0:
                # 현재 여유있는 은보다 더 많은 은이 필요한 경우
                pass
            # elif (dp[rank][s] - (b_diff+1)) < 0:
            #     # 현재 여유있는 동보다 더 많은 동이 필요한 경우
            #     # 이럴 경우 dp의 값이 -1 이하가 되고
            #     # 어차피 max(초기값(-1), 값)에서 걸러짐.
            #     pass
            else:
                dp[rank+1][s-s_diff] = max(
                    dp[rank+1][s-s_diff], dp[rank][s]-(b_diff+1))
        else:
            # 음수라면, 즉 동메달은 내버려둬도 된다면
            if (s_diff) > L:
                pass
            elif (s-s_diff) < 0:
                pass
            else:
                dp[rank+1][s-s_diff] = max(
                    dp[rank+1][s-s_diff], dp[rank][s])

        # s를 더 쓰기
        if (s_diff+1) > L:
            pass
        elif (s-(s_diff+1)) < 0:
            pass
        else:
            dp[rank+1][s-(s_diff+1)] = max(
                dp[rank+1][s-(s_diff+1)], dp[rank][s])


ans = -1
for rank in range(0, N):
    for s in range(0, 10_001):
        if dp[rank][s] != -1:
            ans = rank
print(ans+1)
# 제로 인덱싱
