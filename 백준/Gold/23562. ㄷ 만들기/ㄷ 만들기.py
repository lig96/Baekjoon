import sys
input = sys.stdin.readline


def dim2_range(startr, endr, startc, endc):
    for r in range(startr, endr):
        for c in range(startc, endc):
            yield (r, c)
    # end generator


def make_colored_board():
    for startr, startc in dim2_range(0, R, 0, C):
        # ㄷ의 맨 왼쪽 위의 좌표
        for k in range(1, max_k+1):
            if not (0 <= (startr+2*k+(k-1)) < R and 0 <= (startc+2*k+(k-1)) < C):
                # ㄷ의 맨 오른쪽 아래가 보드의 바깥이라면
                break
            ret = [["." for _ in range(C)] for _ in range(R)]
            for midr, midc in [(startr, startc), (startr, startc+k), (startr, startc+2*k),
                               (startr+k, startc),
                               (startr+2*k, startc), (startr+2*k, startc+k), (startr+2*k, startc+2*k)]:
                # 7개의 작은 정사각형의 맨 왼쪽 위의 좌표
                for r, c in dim2_range(midr, midr+k, midc, midc+k):
                    # 작은 정사각형 안의 r, c 좌표를 칠한다.
                    ret[r][c] = "#"
            yield ret
    # end generator


n, m = map(int, input().split())
R, C = n, m
a, b = map(int, input().split())
# 흰색 칸을 검은색으로 칠하는 데 드는 비용은 a,
# 검은색 칸을 지워서 흰색 칸으로 만드는 데 드는 비용은 b다
board = [list(input().rstrip()) for _ in range(R)]
# #은 검은색으로 칠해진 칸, .은 흰색 칸을 의미한다.


max_k = min(R, C)//3


ans = float('inf')
for colored_board in make_colored_board():
    # 브루트포스로 만든 모든 ㄷ의 크기와 위치별 경우의 수
    temp_ans = 0
    for r, c in dim2_range(0, R, 0, C):
        if board[r][c] == colored_board[r][c]:
            # 색이 동일하다면
            continue
        temp_ans += (a if board[r][c] == "." else b)
    ans = min(ans, temp_ans)


print(ans)
