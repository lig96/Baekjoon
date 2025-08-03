import sys
input = sys.stdin.readline


def new_ans(r, c, d):
    assert d == "r" or d == "c"

    temp = []
    d = 0 if d == "r" else 1
    for i in range([r, c][d], [R, C][d]):
        if board[[i, r][d]][[c, i][d]] == "#":
            break
        temp.append(board[[i, r][d]][[c, i][d]])

    if len(temp) >= 2:
        ans_arr.append(''.join(temp))
    return


R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]


ans_arr = []
for r in range(R):
    for c in range(C):
        if board[r][c] == "#":
            continue
        if r == 0 or (r >= 1 and board[r-1][c] == "#"):
            new_ans(r, c, "r")
        if c == 0 or (c >= 1 and board[r][c-1] == "#"):
            new_ans(r, c, "c")


print(min(ans_arr))
