import sys
input = sys.stdin.readline


def check_ans():
    global area

    if cond_w and cond_h:
        area = max(area, h1*w1+h2*w2)
    return


H, W = map(int, input().split())
N = int(input())
stickers = [list(map(int, input().split())) for _ in range(N)]


area = 0  # -float('inf')
for i1 in range(0, N-1):
    h1, w1 = stickers[i1]
    for i2 in range(i1+1, N):
        h2, w2 = stickers[i2]
        for _ in range(2):
            # 1번 스티커를 회전시킬지
            # 1번 스티커를 그대로 할지
            h1, w1 = w1, h1
            for _ in range(2):
                # 2번 스티커를 회전시킬지
                # 2번 스티커를 그대로 할지
                h2, w2 = w2, h2
                for loc in range(2):
                    # 두 스티커를 가로로 붙일지
                    # 두 스티커를 세로로 붙일지
                    cond_w = (
                        (w1+w2 <= W) if loc == 0 else (max(w1, w2) <= W)
                    )
                    cond_h = (
                        (max(h1, h2) <= H) if loc == 0 else (h1+h2 <= H)
                    )

                    check_ans()


print(area)
