import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def get_ans(rr, cc):
    global ans

    temp = [[None for _ in range(8)] for _ in range(8)]
    for r in range(8):
        for c in range(8):
            temp[r][c] = board[r+rr][c+cc]

    for compare in [correct_W, correct_B]:
        ret = 0
        for r in range(8):
            for c in range(8):
                ret += int(temp[r][c] != compare[r][c])
        ans = min(ans, ret)
    return


R, C = map(int, input().split())
board = [list(input().rstrip())for _ in range(R)]


correct_B = []  # (0, 0) = 'B'
temp = ['B', 'W'] * 4
for _ in range(4):
    correct_B.append(temp)
    correct_B.append(temp[::-1])
correct_W = [x[::-1] for x in correct_B]


ans = float('inf')
for r in range(0, R-8+1):
    for c in range(0, C-8+1):
        get_ans(r, c)


print(ans)
