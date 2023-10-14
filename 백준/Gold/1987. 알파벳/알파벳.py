
import sys
input = sys.stdin.readline


def dfs(graph, v, already, detph=1):
    global ans
    # visited랑 알파벳의 already랑 겹치기 때문에 필요 없음

    r, c = v
    already[ord(graph[r][c])] = True
    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if 0 <= newr < R and 0 <= newc < C and not already[ord(graph[newr][newc])]:
            dfs(graph, (newr, newc), already, detph+1)
    already[ord(graph[r][c])] = False

    # if sum(already)+1 == 26:
    #     print(26)
    #     exit()
    # else:
    ans = max(ans, detph)


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]


ans = 0
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


dfs(graph, (0, 0), [False for _ in range(90+1)])

# for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     print(ord(i))
#     # 65 포함 ~ 90 포함

print(ans)
# 재귀를 끝낸 뒤 시작점을 버린 후 ans를 갱신하기 때문에
# 1을 더해야 한다.
