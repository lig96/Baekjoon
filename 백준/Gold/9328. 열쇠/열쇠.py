# 가장자리만 방문 가능하기 때문에 '.'으로 둘러싸준다.
# 방법 1.
# 눈 앞에서 지나친 door를 저장 후 열쇠를 찾으면 스택/큐에 넣어준다.
# 방법 2.
# 열쇠를 찾으면 visited를 초기화하고 처음부터 그래프 탐색을 한다.


import sys
input = sys.stdin.readline


def dfs(startr, startc):
    global ans

    stack = []
    stack.append((startr, startc))
    visited[startr][startc] = True
    # 시작값은 언제나 '.'이고 not visited

    while stack:
        r, c = stack.pop()
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if not ((0 <= newr < R) and (0 <= newc < C)):
                continue
            if visited[newr][newc]:
                continue

            v = graph[newr][newc]
            if v == '*':
                continue
            elif v == '.':
                do_visit(newr, newc, stack)
            elif v == '$':
                do_visit(newr, newc, stack)
                ans += 1
            elif v == v.lower():
                if v in keys:
                    # 있는 열쇠
                    do_visit(newr, newc, stack)
                else:
                    # 없는 열쇠
                    do_visit(newr, newc, stack)
                    keys.add(v)
                    for door_r, door_c in (deepcopy := tuple(temp for temp in adj_doors)):
                        if graph[door_r][door_c] == v.upper():
                            stack.append((door_r, door_c))
                            adj_doors.remove((door_r, door_c))
            elif v == v.upper():
                if v.lower() in keys:
                    # 열 수 있는 문
                    do_visit(newr, newc, stack)
                else:
                    # 열 수 없는 문
                    adj_doors.add((newr, newc))
                    continue
            else:
                raise Exception('조건 분기 잘못함')
    return


def do_visit(r, c, stack):
    visited[r][c] = True
    graph[r][c] = '.'
    stack.append((r, c))
    return


T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    graph = []
    graph.append(['.' for _ in range(C+2)])
    for _ in range(R):
        temp = ['.']+list(input().rstrip())+['.']
        graph.append(temp)
    graph.append(['.' for _ in range(C+2)])
    R, C = R+2, C+2
    if (temp := input().rstrip()) == '0':
        keys = set()
    else:
        keys = set(temp)

    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    visited = [[False for _ in range(C)] for _ in range(R)]
    adj_doors = set()
    # 현재 방문 가능한 곳들로부터 1칸 차이나는 문

    ans = 0
    dfs(0, 0)

    print(ans)
