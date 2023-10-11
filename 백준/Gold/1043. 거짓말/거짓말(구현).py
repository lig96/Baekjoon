# dfs와 유사한 구현
# https://ku-hug.tistory.com/148
# 1번째 파티에서 거짓말을 했다가 3번째 파티에서 들통이 나는 경우가 있다.
# dfs에서는 일단 거짓말을 하고 나중에 return을 한다.
# 현재 구현의 경우 라인 A에서 M만큼 반복문을 돌면서
# 애초에 첫 파티부터 라인 B를 통해 진실을 말하게 한다.

N, M = map(int, input().split())
yes_arr = list(map(int, input().split()))[1:]
parties = [party for party in
           (list(map(int, input().split()))[1:] for _ in range(M))]
# 몇 명인지는 필요없음
# array.pop(0)도 가능


yes_set = set(yes_arr)


for _ in range(M):  # 라인 A
    for party in parties:
        if yes_set & set(party):
            yes_set = yes_set | set(party)


ans = 0
for party in parties:
    if yes_set & set(party):
        continue  # 라인 B
    else:
        ans += 1


print(ans)
