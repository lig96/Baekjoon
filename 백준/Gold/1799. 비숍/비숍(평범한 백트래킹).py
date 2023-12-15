'''
방법1. 평범한 백트래킹
Python3 -> 10_488ms

12345
67890
abcde
fghij
!@#$%
비숍은 대각선으로 움직인다

->

....5....            -4 - 0
...4.0...            -3 - 1
..3.9.e..            -2 - 2
.2.8.d.j.            -1 - 3
1.7.c.i.% - (r-c) == 0  - 4
.6.b.h.$. - (r-c) == 1  - 5
..a.g.#..            2  - 6
...f.@...            3  - 7
....!....            4  - 8
012345678 - (r+c)
비숍은 좌우, 상하로 움직인다.


N == 10
(1*2*3*4*5*6*7*8*9*10)*(9*8*7*6*5*4*3*2*1)
1_316_818_944_000
1e12


'끝까지 가도 갱신이 불가능한 경우' 조건만 추가하고
평범한 백트래킹을 쓴다.
'''


import sys
input = sys.stdin.readline


def dfs(r, local_ans):
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
        dfs(r+1, local_ans+1)
        visited_c[c] = False
    dfs(r+1, local_ans)
    # 현재 row에서는 아무 칸도 안 쓰고 다음 깊이로
    return


N = int(input())
graph = [[] for _ in range(2*N-1)]
# 희소한 인접 리스트 방식
for r in range(N):
    for c, v in enumerate(list(map(int, input().split()))):
        if v == 1:
            newr, newc = (r-c)+N-1, r+c
            graph[newr].append(newc)


ans = 0
visited_c = [False for _ in range(2*N-1)]


dfs(r=0, local_ans=0)


print(ans)
