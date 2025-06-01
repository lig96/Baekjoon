from collections import deque
import sys
input = sys.stdin.readline


class Dice():
    def __init__(self):
        self.top = 1
        self.north = 2
        self.east = 3
        self.west = 4
        self.south = 5
        self.bottom = 6
        self.direction = 0  # 동서남북 = 0123
        self.location = (0, 0)  # 제로 인덱싱

        self.dr = [0, 0, 1, -1]
        self.dc = [1, -1, 0, 0]
        self.opposite_direction = [1, 0, 3, 2]
        self.clockwise_direction = [2, 3, 1, 0]
        return

    def move(self):
        r, c = self.location
        d = self.direction
        newr, newc = r+self.dr[d], c+self.dc[d]
        if not (0 <= newr < N and 0 <= newc < M):
            d = self.opposite_direction[d]
            newr, newc = r+self.dr[d], c+self.dc[d]
        # 주사위가 이동 방향으로 한 칸 굴러간다.
        # 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.

        if d == 0:  # 동
            self.top, self.east, self.bottom, self.west = (
                self.west, self.top, self.east, self.bottom
            )
        elif d == 1:  # 서
            self.top, self.east, self.bottom, self.west = (
                self.east, self.bottom, self.west, self.top
            )
        elif d == 2:  # 남
            self.north, self.top, self.south, self.bottom = (
                self.bottom, self.north, self.top, self.south
            )
        elif d == 3:  # 북
            self.north, self.top, self.south, self.bottom = (
                self.top, self.south, self.bottom, self.north
            )
        else:
            raise Exception
        # 주사위가 한 칸 굴러감에 따라 전개도의 위치가 바뀐다.

        self.location = (newr, newc)
        self.direction = d
        # 주사위의 속성이 달라진다.
        return

    def change_direction(self):
        A = self.bottom
        B = board[self.location[0]][self.location[1]]
        if A > B:
            self.direction = self.clockwise_direction[self.direction]
        elif A < B:
            for _ in range(3):
                self.direction = self.clockwise_direction[self.direction]
                # 90도 3번 = 270도 = -90도
    # end class


def bfs(visited, r, c, flood_i, value, dr, dc):
    cnt = 0
    dq = deque()

    cnt += 1
    visited[r][c] = flood_i
    dq.append((r, c))

    while dq:
        r, c = dq.popleft()
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if not (0 <= newr < N and 0 <= newc < M):
                continue
            if visited[newr][newc] != -1:
                continue
            if board[newr][newc] != value:
                continue
            cnt += 1
            visited[newr][newc] = flood_i
            dq.append((newr, newc))
    return cnt


def make_C_board():
    ''' C_board[r][c] = board[r][c]에서부터 이동할 수 있는 칸의 수 C'''
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    C_dict = {}
    C_board = [[None for _ in range(M)] for _ in range(N)]
    flood_i = 0
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    for r in range(N):
        for c in range(M):
            if visited[r][c] == -1:
                cnt = bfs(visited, r, c, flood_i, board[r][c], dr, dc)
                C_dict[flood_i] = cnt
                flood_i += 1
            C_board[r][c] = C_dict[visited[r][c]]
    return C_board


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


dice = Dice()
C_board = make_C_board()


score = 0
for _ in range(K):
    dice.move()
    score += (board[dice.location[0]][dice.location[1]] *
              C_board[dice.location[0]][dice.location[1]])
    dice.change_direction()


print(score)
