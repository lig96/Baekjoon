import sys
input = sys.stdin.readline


def make_dictionaries():
    # 시작=0
    # 1                        도착=32
    # 2                        27        31   30
    # 3                        26               29
    # 4                        25                 28
    # 파랑=5        11 12 13 /14/ 22 23 24          파랑=21
    # 6                                             20
    #    7                                     19
    #        8                 16         18
    #            9             15   17
    #                    파랑=10
    #
    # nxt_keys = list(range(0, 32+1))  # 0<=x<=32
    # print([(v, ) for v in nxt_keys])
    # 이후 수작업으로 변경

    nxt_keys_and_values = [
        (0, 1), (1, 2), (2, 3),
        (3, 4), (4, 5), (5, 6),
        (6, 7), (7, 8), (8, 9),
        (9, 10), (10, 17), (11, 12),
        (12, 13), (13, 14), (14, 25),
        (15, 16), (16, 14), (17, 18),
        (18, 19), (19, 20), (20, 21),
        (21, 28), (22, 14), (23, 22),
        (24, 23), (25, 26), (26, 27),
        (27, 32), (28, 29), (29, 30),
        (30, 31), (31, 27), (32, 32)
    ]
    nxt = dict(nxt_keys_and_values)
    # nxt[start_id] = end_id, start_id가 파란색이 아닐 때

    nxt_blue_keys_and_values = [
        (5, 11), (10, 15), (21, 24)
    ]
    nxt_blue = dict(nxt_blue_keys_and_values)
    # nxt_blue[start_id] = end_id, start_id가 파란색일 때

    score_keys_and_values = [
        (0, None), (1, 2), (2, 4),
        (3, 6), (4, 8), (5, 10),
        (6, 12), (7, 14), (8, 16),
        (9, 18), (10, 20), (11, 13),
        (12, 16), (13, 19), (14, 25),
        (15, 22), (16, 24), (17, 22),
        (18, 24), (19, 26), (20, 28),
        (21, 30), (22, 26), (23, 27),
        (24, 28), (25, 30), (26, 35),
        (27, 40), (28, 32), (29, 34),
        (30, 36), (31, 38), (32, 0)
    ]
    score = dict(score_keys_and_values)
    # score[x_id] = score of x position in the board
    return nxt, nxt_blue, score


def sol(used_dices_cnt, temp_tot_score):
    def move():
        now_pos = pieces_positions[now_piece]
        if now_pos == END:
            return None, None

        for i in range(now_dice):
            if i == 0 and now_pos in nxt_blue.keys():
                now_pos = nxt_blue[now_pos]
            else:
                now_pos = nxt[now_pos]
            if now_pos == END:
                # 도착 칸으로 이동하면 (...) 이동을 마친다.
                break

        final_pos = now_pos
        if final_pos in pieces_positions and final_pos != END:
            return None, None
        pieces_positions[now_piece] = final_pos
        return "Not None", score[final_pos]

    if used_dices_cnt == 10:
        global max_tot_score
        max_tot_score = max(max_tot_score, temp_tot_score)
        return

    for now_piece in range(4):
        # 4개 중에 움직일 말
        now_dice = dices[used_dices_cnt]
        # 이번 차례에 사용할 주사위

        old_pos: int = pieces_positions[now_piece]
        result, added_score = move()
        if result is not None:
            # 움직일 수 있다면
            sol(used_dices_cnt+1, temp_tot_score+added_score)
            pieces_positions[now_piece] = old_pos
    return


dices = list(map(int, input().split()))


nxt, nxt_blue, score = make_dictionaries()
START, END = 0, 32
max_tot_score = -float('inf')
pieces_positions = [START for _ in range(4)]


sol(0, 0)


print(max_tot_score)
