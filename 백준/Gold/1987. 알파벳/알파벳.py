# 기존에 거쳐온 알파벳들을 저장하기 위해
# set와 list 모두 사용 가능한데 둘 다 O(1)이지만 list가 빠르다.

import sys
input = sys.stdin.readline


def dfs(graph, v, already, depth):
    global ans
    # visited랑 알파벳의 already랑 겹치기 때문에 필요 없음

    r, c = v
    already[ord(graph[r][c])] = True
    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if 0 <= newr < R and 0 <= newc < C and not already[ord(graph[newr][newc])]:
            dfs(graph, (newr, newc), already, depth+1)
    already[ord(graph[r][c])] = False

    # if depth == biggest:
    #     print(depth)
    #     exit()
    # else:
    #     ans = max(ans, depth)
    # 조기 종료로 절약되는 시간보다
    # 크기 비교 때문에 소모되는 시간이 긴 듯하다.

    ans = max(ans, depth)
    return


R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
# biggest = len(set([x for y in graph for x in y]))


ans = 0
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


dfs(graph, (0, 0), [False for _ in range(90+1)], 1)


print(ans)
