import sys
print = sys.stdout.write


def rec(depth, row, col):
    if depth == 1:
        board[row][col] = '*'
        return

    ROW = ((2 ** (depth))*1)-1
    COL = ((2 ** (depth-1)))*4-3

    n_ROW = ((2 ** (depth-1))*1)-1
    n_COL = ((2 ** (depth-1-1)))*4-3

    if depth % 2 == 0:
        # 짝수라면
        for i in range(COL):
            board[row][col+i] = '*'
            # 가로 선
        for i in range(ROW):
            board[row+i][col+COL-1-i] = '*'
            # 우상향 선
        for i in range(ROW):
            board[row+i][col+i] = '*'
            # 우하향 선
        rec(depth-1, row+n_ROW, col+(COL-n_COL)//2)
    else:
        # 홀수라면
        for i in range(COL):
            board[row][col+i] = '*'
            # 가로 선
        for i in range(ROW):
            board[row-i][col+i] = '*'
            # 우상향 선
        for i in range(ROW):
            board[row-i][col+COL-1-i] = '*'
            # 우하향 선
        rec(depth-1, row-n_ROW, col+(COL-n_COL)//2)


N = int(input())


ROW = ((2 ** (N))*1)-1
COL = ((2 ** (N-1)))*4-3
board = [[' ' for _ in range(COL)] for _ in range(ROW)]


if N % 2 == 0:
    # 짝수라면
    rec(N, 0, 0)
else:
    # 홀수라면
    rec(N, ROW-1, 0)


for i in board:
    print(''.join(i).rstrip()+'\n')
