# DFS
# https://4legs-study.tistory.com/94
'''
내가 주황색으로 표시된 사람과 친구 관계가 될 수 있을지는 어떻게 알 수 있을까?
친구 관계를 그래프로 나타낸 후 나를 시작으로 그래프 탐색(DFS, BFS)을 통해
만약 주황색으로 표시된 친구 관계가 새로 생겼다고 할 때,
우리는 주황색 사람과 친구 관계가 될 수 있는지 알기 위해서다시 그래프 탐색을 진행해야 한다.
'''
# DFS가 아닌 union-find 방식으로 풀어야 한다.

N, M = map(int, input().split())
yes_arr = list(map(int, input().split()))[1:]
parties = [party for party in
           (list(map(int, input().split()))[1:] for _ in range(M))]
# 몇 명인지는 필요없음
# array.pop(0)도 가능


def dfs(yes, no, level, ans):
    if level == M:
        # 012, 총 3파티를 끝내고 다음 깊이로 들어갈 때 종료
        ans_arr.append(ans)
        return

    current = parties[level]
    if set(current) & yes:
        # 현재 인원과 진실이 겹친다면
        # 무조건 진실
        if set(current) & no:
            # 현재 인원과 거짓이 겹친다면
            # 진실을 말하면 거짓이 들통남
            # 둘 다 불가능
            return
        else:
            # 진실만 가능
            dfs(set(current) | yes, no, level+1, ans)  # 진실
    else:
        # 현재 인원과 진실이 겹치지 않는다면
        # 진실, 거짓 둘 다 가능
        if set(current) & no:
            # 현재 인원과 거짓이 겹친다면
            # 진실 불가능, 거짓만 가능
            dfs(yes, set(current) | no, level+1, ans+1)  # 거짓
        else:
            # 진실 가능, 거짓 가능
            dfs(yes, set(current) | no, level+1, ans+1)  # 거짓
            dfs(set(current) | yes, no, level+1, ans)  # 진실


ans_arr = []
dfs(set(yes_arr), set(), 0, 0)


print(max(ans_arr))
