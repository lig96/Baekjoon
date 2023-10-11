# union-find 방식


def find(v):
    if parent[v] == v:
        pass
    else:
        parent[v] = find(parent[v])
    return parent[v]


def union(v_a, v_b):
    a, b = find(v_a), find(v_b)
    parent[a], parent[b] = min(a, b), min(a, b)
    return


N, M = map(int, input().split())
yes_arr = list(map(int, input().split()))[1:]
parties = [party for party in
           (list(map(int, input().split()))[1:] for _ in range(M))]
# 몇 명인지는 필요없음
# array.pop(0)도 가능


parent = [i for i in range(N+1)]
[union(0, yes) for yes in yes_arr]
# 인덱스를 맞추기 위해 N+1
# 0번 인덱스는 이미 진실을 아는 사람들


for party in parties:
    for person in party:
        union(party[0], person)
        # 파티의 0번째 인물과 파티의 n번째 인물


ans = 0
for party in parties:
    for people in party:
        if find(0) == find(people):
            break
    else:
        ans += 1
    # for문이 정상적으로 끝났다면 else문을 실행하고
    # break 되었다면 else문을 실행하지 않는다.
    # 호불호가 갈리지만 별도의 flag 없이 코딩할 수 있다.


print(ans)
