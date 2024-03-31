import sys
input = sys.stdin.readline


def sol(rule, games):
    ret = 0
    for a, b in games:
        if rule[a] == b:
            # a가 이기는 것이 b라면
            ret += 1
    return ret


N = int(input())
games = [list(map(int, input().split())) for _ in range(N)]


rules = [(1, 2, 3), (1, 3, 2),
         (2, 1, 3), (2, 3, 1),
         (3, 1, 2), (3, 2, 1)]
# (1, 2, 3) -> 3 beats 2, 2 beats 1, 1 beats 3
# 마이너스 인덱싱 쓰려고 오른쪽에서 왼쪽으로.
rules = [{rule[i]: rule[i-1] for i in range(3)} for rule in rules]
# {1: 3, 2: 1, 3: 2} -> 1 beats 3, 2 beats 1, 3 beats 2


cnt = -1
for rule in rules:
    temp_cnt = sol(rule, games)
    cnt = max(cnt, temp_cnt)


print(cnt)
