import sys
input = sys.stdin.readline


N, A, B = map(int, input().split())
alice = list(map(int, input().split()))
bob = list(map(int, input().split()))


dic = dict()
for x in alice:
    dic[x] = 'alice'
for x in bob:
    if x in dic:
        dic[x] = 'both'
    else:
        dic[x] = 'bob'
tot = sorted(dic.items())


ans = float('inf')
for now in ['alice', 'bob']:
    # 첫 시작이 누구인지 정함.
    # 아예 못 푸는 경우를 뺐듯이 'both'인 경우도 tot에서 빼면
    # 무조건 시작이 tot[0][1]으로 고정이 돼서 조금 더 빠름.
    temp = 0
    for _, can_solve in tot:
        if can_solve == 'both':
            pass
        elif can_solve == now:
            pass
        elif can_solve != now:
            temp += 1
            now = can_solve
    ans = min(ans, temp)


print(ans)
