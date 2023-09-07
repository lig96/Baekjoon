import sys
input = sys.stdin.readline


ROW, COL = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(ROW)]


shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # 청록
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # 노랑
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # 주황
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # 초록
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # 보라
]


ans = 0
for _1 in range(4):
    # 오른쪽으로 90도 회전
    mat = [list(rows[::-1]) for rows in zip(*mat)]
    for _2 in range(2):
        # 위아래 대칭
        mat = mat[::-1]
        for r in range(len(mat)):
            # 회전 시키는 과정에서 row의 최댓값이
            # ROW, COL 사이로 변화함.
            for c in range(len(mat[0])):
                for shape in shapes:
                    try:
                        temp = sum([mat[r+dr][c+dc] for dr, dc in shape])
                        ans = max(ans, temp)
                    except:
                        pass
print(ans)
