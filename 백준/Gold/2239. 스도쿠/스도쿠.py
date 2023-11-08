def dfs(board, r, c):
    if c == 9:
        dfs(board, r+1, 0)
        return
    elif (r, c) == (9, 0):
        for i in board:
            print(*i, sep='')
        exit()
        return

    if board[r][c] == 0:
        for i in range(1, 10):
            if set_r[r][i]:
                continue
            if set_c[c][i]:
                continue
            if set_box[box(r, c)][i]:
                continue
            # 셋 모두 아니라면
            set_r[r][i] = True
            set_c[c][i] = True
            set_box[box(r, c)][i] = True
            board[r][c] = i
            dfs(board, r, c+1)
            set_r[r][i] = False
            set_c[c][i] = False
            set_box[box(r, c)][i] = False
            board[r][c] = 0
    else:
        dfs(board, r, c+1)


def box(r, c):
    return (r//3)*3 + (c//3)


board = [list(map(int, list(input()))) for _ in range(9)]


set_r = [[False for _ in range(10)] for _ in range(9)]
set_c = [[False for _ in range(10)] for _ in range(9)]
set_box = [[False for _ in range(10)] for _ in range(9)]
for r in range(9):
    for c in range(9):
        num = board[r][c]
        set_r[r][num] = True
        set_c[c][num] = True
        set_box[box(r, c)][num] = True
# box
# 012
# 345
# 678


dfs(board, 0, 0)
