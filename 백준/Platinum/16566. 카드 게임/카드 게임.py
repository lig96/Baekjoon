# enemy_card보다 첫 번째로 큰 정수

# 방법 1.
# union-find를 써서 O(K*N)보다 시간을 절약한다.
# my_cards에 있으면 자기 자신을 가리키고
# 없거나 소진을 했으면 오른쪽을 가리킨다.


import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(int(4e6)+50)


def find(x):
    if parent[x] != x:  # 라인 A
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if True:
        # 언제나 왼쪽이 오른쪽을 가리키게
        parent[a] = b
    return


N, M, K = map(int, input().split())
my_cards = list(map(int, input().split()))
enemy_cards = list(map(int, input().split()))


parent = [i+1 for i in range(N+2)]
for my_card in my_cards:
    parent[my_card] = my_card
parent[N+1] = N+1
# 쿼리 enemy_card의 최댓값은 N-1
# 해당 쿼리에서 나오는 ans는 N
# union(ans, ans+1)이기 때문에
# parent를 N+1까지 선언하고 라인 A 인덱스에러를 막기 위해
# 자기 자신으로 대입. 이걸 안 하면 끝 없이 오른쪽으로
# 향하다가 parent[매우큰숫자]를 하고 에러가 남.


for enemy_card in enemy_cards:
    ans = find(enemy_card+1)  # 초과를 찾는 것이니 +1
    union(ans, ans+1)

    print(str(ans)+'\n')
