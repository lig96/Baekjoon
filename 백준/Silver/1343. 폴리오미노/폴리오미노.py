import sys
input = sys.stdin.readline


def sol(board):
    def can_fill(string, board, i):
        if board[i:i+len(string)] == ['X' for _ in range(len(string))]:
            return True
        return False

    def fill(string, board, i):
        board[i:i+len(string)] = list(string)
        return

    board = list(board)
    for i in range(len(board)):
        if board[i] != "X":
            continue

        if can_fill("AAAA", board, i):
            fill("AAAA", board, i)
        elif can_fill("BB", board, i):
            fill("BB", board, i)
        else:
            return "-1"
    return "".join(board)


def sol_2(board):
    board = board.replace("XXXX", "AAAA")
    board = board.replace("XX", "BB")

    return '-1' if 'X' in board else board


board = input().rstrip()


# print(sol(board))
print(sol_2(board))
