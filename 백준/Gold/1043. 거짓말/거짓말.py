
N, M = map(int, input().split())
temp = list(map(int, input().split()))
already_cnt, already_arr = temp[0:1], temp[1:]
parties = []
for _ in range(M):
    temp = list(map(int, input().split()))
    party_cnt, party_arr = temp[0:1], temp[1:]
    parties.append((party_cnt, party_arr))
# print(parties)


def dfs(yes, no, level, ans):
    if level == M:
        # 012, 총 3파티를 끝내고
        # 다음 깊이로 들어갈 때 종료
        ans_arr.append(ans)
        return

    cnt, current = parties[level]
    # print('@@@@@')
    # print(set(current))
    # print(yes)
    # print(no)
    # print(set(current) & yes)
    # print('@@@@@@@@@@@@@')
    if set(current) & yes:
        # 현재 인원과 진실이 겹친다면
        # 무조건 진실을 말해야 함
        if set(current) & no:
            # 현재 인원과 거짓이 겹친다면
            # 진실을 말하면 거짓이 들통남
            # 둘 다 불가능
            return
        else:
            dfs(set(current) | yes, no, level+1, ans)
            # 진실만 가능
    else:
        # 현재 인원과 진실이 겹치지 않는다면
        # 진실, 거짓 둘 다 가능
        if set(current) & no:
            # 현재 인원과 거짓이 겹친다면
            # 진실 불가능, 거짓만 가능
            dfs(yes, set(current) | no, level+1, ans+1)
            # 거짓
        else:
            # 진실, 거짓 둘 다 가능
            dfs(yes, set(current) | no, level+1, ans+1)
            # 거짓
            dfs(set(current) | yes, no, level+1, ans)
            # 진실


ans_arr = []
dfs(set(already_arr), set(), 0, 0)
print(max(ans_arr))
# print(ans_arr)
