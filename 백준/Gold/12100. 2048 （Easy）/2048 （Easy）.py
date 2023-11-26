def dfs(board, level):
    if level == 5:
        check(board)
        return

    for i in range(4):  # 우, 좌, 하, 상
        dfs(move(board, i), level+1)
    return


def move(board, i):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    if i == 0:
        for r in range(N):
            index = N-1
            for c in range(N)[::-1]:
                if board[r][c] != 0:
                    if temp[r][index] == 0:
                        temp[r][index] = board[r][c]
                    elif temp[r][index] == board[r][c]:
                        temp[r][index] = board[r][c]*2
                        index -= 1
                    elif temp[r][index] != board[r][c]:
                        index -= 1
                        temp[r][index] = board[r][c]
    elif i == 1:
        for r in range(N):
            index = 0
            for c in range(N):
                if board[r][c] != 0:
                    if temp[r][index] == 0:
                        temp[r][index] = board[r][c]
                    elif temp[r][index] == board[r][c]:
                        temp[r][index] = board[r][c]*2
                        index += 1
                    elif temp[r][index] != board[r][c]:
                        index += 1
                        temp[r][index] = board[r][c]
    elif i == 2:
        for c in range(N):
            index = N-1
            for r in range(N)[::-1]:
                if board[r][c] != 0:
                    if temp[index][c] == 0:
                        temp[index][c] = board[r][c]
                    elif temp[index][c] == board[r][c]:
                        temp[index][c] = board[r][c]*2
                        index -= 1
                    elif temp[index][c] != board[r][c]:
                        index -= 1
                        temp[index][c] = board[r][c]
    elif i == 3:
        for c in range(N):
            index = 0
            for r in range(N):
                if board[r][c] != 0:
                    if temp[index][c] == 0:
                        temp[index][c] = board[r][c]
                    elif temp[index][c] == board[r][c]:
                        temp[index][c] = board[r][c]*2
                        index += 1
                    elif temp[index][c] != board[r][c]:
                        index += 1
                        temp[index][c] = board[r][c]
    return temp


def check(mat):
    global ans

    temp = max(map(max, mat))
    if temp > ans:
        ans = temp
        if ans == max_ans:
            print(ans)
            exit()


N = int(input())
board = [list(map(int,  input().split())) for _ in range(N)]


max_ans = sum(map(sum, board))  # 42
max_ans &= 1 << max_ans.bit_length()-1  # 32


ans = 0
dfs(board, 0)


print(ans)
