from collections import Counter
import sys
input = sys.stdin.readline


def cast_firestorm(L_q):
    temp = [[0 for _ in range(N2)] for _ in range(N2)]
    length = 2**L_q

    for r in range(0, N2, length):
        for c in range(0, N2, length):
            for rr in range(length):
                for cc in range(length):
                    temp[r + cc][c + (length-1) - rr] = board[r + rr][c + cc]

    return temp


def melt_ice():
    def condition():
        cnt = 0
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < N2 and 0 <= newc < N2):
                continue
            if board[newr][newc] > 0:
                cnt += 1
        if cnt >= 3:
            return False
        return True
    temp = [x[::] for x in board]
    for r in range(N2):
        for c in range(N2):
            if board[r][c] > 0 and condition():
                temp[r][c] -= 1
    return temp


def flood_fill():
    def flood_fill_(r, c, ind):
        stack = []
        visited[r][c] = ind
        stack.append((r, c))
        while stack:
            r, c = stack.pop()
            for i in range(4):
                newr, newc = r+dr[i], c+dc[i]
                if not (0 <= newr < 2**N and 0 <= newc < 2**N):
                    continue
                if visited[newr][newc] == -1 and board[newr][newc] > 0:
                    visited[newr][newc] = ind
                    stack.append((newr, newc))
        return
    visited = [[-1 for _ in range(N2)] for _ in range(N2)]
    flood_fill_index = 0
    for r in range(N2):
        for c in range(N2):
            if visited[r][c] == -1 and board[r][c] > 0:
                flood_fill_(r, c, flood_fill_index)
                flood_fill_index += 1
    return visited


N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
firestorms = list(map(int, input().split()))


N2 = 2**N
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


for L_q in firestorms:
    board = cast_firestorm(L_q)
    board = melt_ice()
summation = sum(map(sum, board))
flood_fill_cnt = Counter(tuple(
    x for xx in flood_fill() for x in xx
))
del flood_fill_cnt[-1]  # -1은 flood_fill의 인덱스가 아니라 방문되지 않은 곳이다.
# if -1 in flood_fill_cnt:
#     flood_fill_cnt.pop(-1)


print(summation)
print(flood_fill_cnt.most_common(1)[0][1] if flood_fill_cnt else 0)
