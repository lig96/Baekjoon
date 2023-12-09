# 파이썬으로는 시간 초과가 나서 pypy로 제출하였다.
# dr, dc는 리스트가 아닌 튜플일 때,
# sharks는 딕셔너리가 아닌 이중 리스트일 때
# 약간이나마 속도가 빨랐다.


import sys
input = sys.stdin.readline


def catch(human, sharks):
    nearest_shark = False
    for loop_r in range(R):
        value = sharks[loop_r][human]
        if value:
            nearest_shark = value
            break

    if nearest_shark:
        r, c, s, d, z = nearest_shark
        sharks[r][c] = False
        # sharks는 call by object-reference
        return z
    else:
        return 0


def move_shark(sharks):
    new_sharks = [[False for _ in range(C)] for _ in range(R)]
    for loop_r in range(R):
        for loop_c in range(C):
            shark = sharks[loop_r][loop_c]
            if not shark:
                continue
            r, c, s, d, z = shark

            pure_s = s % (2*(R-1)) if d <= 2 else s % (2*(C-1))
            for _ in range(pure_s):
                newr, newc = r+dr[d], c+dc[d]
                if not (0 <= newr < R) or not (0 <= newc < C):
                    d = change_d(d)
                    newr, newc = r+dr[d], c+dc[d]
                r, c = newr, newc

            temp = new_sharks[r][c]
            if temp:
                if z > temp[4]:
                    new_sharks[r][c] = (r, c, s, d, z)
            else:
                new_sharks[r][c] = (r, c, s, d, z)

    return new_sharks


def change_d(d):
    # return d + (d % 2) - ((d+1) % 2)
    # 느린 듯하다.
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    else:
        return 3


R, C, M = map(int, input().split())
sharks = [[False for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = list(map(int, input().split()))
    r, c = r-1, c-1
    sharks[r][c] = (r, c, s, d, z)
# 1인 경우는 위, 2인 경우는 아래,
# 3인 경우는 오른쪽, 4인 경우는 왼쪽


dr, dc = (None, -1, 1, 0, 0), (None, 0, 0, 1, -1)
human = -1


ans = 0
for _ in range(C):
    human += 1
    ans += catch(human, sharks)
    sharks = move_shark(sharks)


print(ans)
