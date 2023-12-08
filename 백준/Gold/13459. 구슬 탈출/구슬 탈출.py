from collections import deque
import sys
input = sys.stdin.readline


def bfs(board, start_b, start_r):
    visited = set()
    qu = deque()
    visited.add((start_b, start_r))
    qu.append((start_b, start_r, 0))

    while qu:
        b, r, level = qu.popleft()
        if level == 10:
            return 0
        for i in range(4):
            temp_br = move(board, i, b, r)
            if type(temp_br) == tuple and temp_br not in visited:
                new_b, new_r = temp_br
                visited.add((new_b, new_r))
                qu.append((new_b, new_r, level+1))
            elif temp_br == 'True':
                # 움직이는 과정에서 성공한 경우
                return 1
            elif temp_br == 'False':
                # 움직이는 과정에서 실패한 경우
                pass
    return 0


def move(board, i, blue, red):
    is_red_in_hole = False

    r, c = blue
    while True:
        newr, newc = r+dr[i], c+dc[i]
        now = board[newr][newc]
        if now == '#':
            # 벽에 닿았으니 r, c 유지하고 탈출
            break
        elif (newr, newc) == red:
            # 사실상 벽에 닿았으니
            break
        elif now == 'O':
            # 실패 확정
            return 'False'
        elif now == '.':
            # r, c 갱신하고 반복문 계속 돔
            r, c = newr, newc
    blue = (r, c)

    r, c = red
    while True:
        newr, newc = r+dr[i], c+dc[i]
        now = board[newr][newc]
        if now == '#':
            # 벽에 닿았으니 r, c 유지하고 탈출
            break
        elif (newr, newc) == blue:
            # 사실상 벽에 닿았으니
            break
        elif now == 'O':
            # 성공 가능성 있음
            # 구멍에 빠트려서 없애버리고
            # 미래의 파란 구슬의 길을 터줌
            is_red_in_hole = True
            r, c = None, None
            break
        elif now == '.':
            # r, c 갱신하고 반복문 계속 돔
            r, c = newr, newc
    red = (r, c)

    r, c = blue
    while True:
        newr, newc = r+dr[i], c+dc[i]
        now = board[newr][newc]
        if now == '#':
            # 벽에 닿았으니 r, c 유지하고 탈출
            break
        elif (newr, newc) == red:
            # 사실상 벽에 닿았으니
            break
        elif now == 'O':
            # 실패 확정
            return 'False'
        elif now == '.':
            # r, c 갱신하고 반복문 계속 돔
            r, c = newr, newc
    blue = (r, c)
    # 막힐 수 있으니 A, B, A 방식으로 돌려야 함

    if is_red_in_hole:
        return 'True'
    else:
        return blue, red


R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]


for r in range(R):
    for c in range(C):
        if board[r][c] == 'B':
            blue = (r, c)
            board[r][c] = '.'
        elif board[r][c] == 'R':
            red = (r, c)
            board[r][c] = '.'
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
# 오른쪽, 왼쪽, 아래, 위


print(bfs(board, blue, red))
