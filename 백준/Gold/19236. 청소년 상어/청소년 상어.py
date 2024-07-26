import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def move_shark(r, c, d, board, temp_ans):
    eatten_fish = board[r][c]
    board[r][c] = ['shark', None]  # 보드 변경
    # 무조건 생선이 존재함. None이 아니라서 밑의 연산 가능
    temp_ans += eatten_fish[0]  # 잡아먹기
    d = eatten_fish[1]  # 방향 흡수

    for fish_i in range(1, 17):
        temprc = find_rc(fish_i, board)
        if temprc is None:
            continue
        move_fish(temprc[0], temprc[1], board)

    flag_shark_move = False
    for i in range(1, 4):
        # 상어가 이동할 수 있는 칸은 최대 3칸
        newsharkr, newsharkc = r+dr[d]*i, c+dc[d]*i
        if not (0 <= newsharkr < 4 and 0 <= newsharkc < 4):
            continue
        if board[newsharkr][newsharkc] == [None, None]:
            continue
        flag_shark_move = True
        board[r][c] = [None, None]
        move_shark(newsharkr, newsharkc, d,
                   [[x[::] for x in xx] for xx in board], temp_ans)
        board[r][c] = ['shark', None]

    if not flag_shark_move:
        global ans
        ans = max(ans, temp_ans)
        return

    return


def find_rc(target, board):
    for r in range(4):
        for c in range(4):
            if board[r][c][0] == target:
                return (r, c)
    # 없는 경우
    return None


def move_fish(r, c, board):
    # r,c에 있는 생선이 이동을 개시
    for _ in range(8):
        d = board[r][c][1]
        newr, newc = r+dr[d], c+dc[d]
        if (not (0 <= newr < 4 and 0 <= newc < 4)) or (board[newr][newc] == ['shark', None]):
            board[r][c][1] = (d+1) % 8
            continue
        board[r][c], board[newr][newc] = board[newr][newc], board[r][c]
        # 스왑
        return
    # 8번 방향을 바꿨는데도 스왑이 안 됐으면 그냥 리턴
    # 이런 경우는 없음
    return


board = [[None for _ in range(4)] for _ in range(4)]
fish_ds = [None for _ in range(17)]  # 번호는 원인덱싱
for r in range(4):
    temp = list(map(int, input().split()))
    for c in range(4):
        fish_i, fish_d = (temp[c*2], temp[c*2+1]-1)  # 방향은 제로인덱싱
        board[r][c] = [fish_i, fish_d]
# 방향 bi는 8보다 작거나 같은 자연수를 의미하고,
# 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미
# ->
# 0부터         ↑, ↖, ←, ↙, ↓, ↘, →, ↗


# d = (d+1) % 8
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


ans = -float('inf')
move_shark(0, 0, None, board, 0)


print(ans)
