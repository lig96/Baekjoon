'''
방법2. 기발한 백트래킹
Python3 -> 128ms

12345
67890
abcde
fghij
!@#$%
비숍은 대각선으로 움직인다

->

....5....            -4 - 0
.........            -3 - 1
..3.9.e..            -2 - 2
.........            -1 - 3
1.7.c.i.% - (r-c) == 0  - 4
......... - (r-c) == 1  - 5
..a.g.#..            2  - 6
.........            3  - 7
....!....            4  - 8
012345678 - (r+c)
(r+c)가 짝수인 경우
비숍은 좌우, 상하로 움직인다.

.........            -4 - 0
...4.0...            -3 - 1
.........            -2 - 2
.2.8.d.j.            -1 - 3
......... - (r-c) == 0  - 4
.6.b.h.$. - (r-c) == 1  - 5
.........            2  - 6
...f.@...            3  - 7
.........            4  - 8
012345678 - (r+c)
(r+c)가 홀수인 경우
비숍은 좌우, 상하로 움직인다.


N == 10
(1*3*5)*(3*1), (2*4)*(4*2)
109
(엄밀히 말하면 특정 row에서 1개를 선택할 뿐만 아니라
선택 안 하는 선택지도 있으니 각각에 +1을 더해줘야 함)
(대각선을 활용 안 했을 때보다는 훨씬 적다.
2^100 = (2^10)^10 = 1e30)
(동일한 방식에서 홀짝을 안 나눴을 때보다는 훨씬 적다.
1을 안 더하면 1e12, 1을 더하면 1e15)

'끝까지 가도 갱신이 불가능한 경우' 조건을 추가하고
기발한 발상의 백트래킹을 쓴다.

비숍은 언제나 대각선 방향만 움직이기 때문에
하얀 비숍은 언제나 하얗고 까만 비숍은 언제나 까맣다.
굳이 홀수인 5에서 시작하며 dfs를 돌면서
짝수인 4, 0을 포함할지 안 할지 신경쓸 필요 없다.
홀수 비숍의 최댓값 + 짝수 비숍의 최댓값을 구해준다.
'''
import sys
input = sys.stdin.readline


def dfs(r, local_ans, graph):
    global ans

    if r == 2*N-1:
        # 깊이를 끝까지 간 경우
        if ans < local_ans:
            ans = local_ans
        return

    # 깊이가 끝이 아닌 경우
    if (local_ans + ((2*N-1)-r)) <= ans:
        # 끝까지 가도 갱신이 불가능한 경우
        return
    # 끝까지 가면 아마도 갱신이 가능한 경우
    for c in graph[r]:
        if visited_c[c]:
            # 세로줄을 이미 썼을 경우
            continue
        # 언제나 visited_r[r]은 False

        visited_c[c] = True
        dfs(r+1, local_ans+1, graph)
        visited_c[c] = False
    dfs(r+1, local_ans, graph)
    # 현재 row에서는 아무 칸도 안 쓰고 다음 깊이로
    return


N = int(input())
odd_graph = [[] for _ in range(2*N-1)]
even_graph = [[] for _ in range(2*N-1)]
# 희소한 인접 리스트 방식
for r in range(N):
    for c, v in enumerate(list(map(int, input().split()))):
        if v == 1:
            if (r+c) % 2 == 0:
                newr, newc = (r-c)+N-1, r+c
                even_graph[newr].append(newc)
            else:
                newr, newc = (r-c)+N-1, r+c
                odd_graph[newr].append(newc)


total_ans = 0

ans = 0
visited_c = [False for _ in range(2*N-1)]
dfs(r=0, local_ans=0, graph=odd_graph)
total_ans += ans

ans = 0
visited_c = [False for _ in range(2*N-1)]
dfs(r=0, local_ans=0, graph=even_graph)
total_ans += ans


print(total_ans)
