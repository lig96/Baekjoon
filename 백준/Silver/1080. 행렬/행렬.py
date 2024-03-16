import sys
input = sys.stdin.readline


def do_flip(startr, startc, mat):
    global ans

    ans += 1

    for r in range(startr, startr+3):
        for c in range(startc, startc+3):
            mat[r][c] = 0 if mat[r][c] == 1 else 1
    # 객체 참조에 의한 호출
    return


def is_same(A, B):
    for r in range(R):
        for c in range(C):
            if A[r][c] != B[r][c]:
                return False
    return True


R, C = map(int, input().split())  # N, M
A = [list(map(int, input().rstrip())) for _ in range(R)]
B = [list(map(int, input().rstrip())) for _ in range(R)]


ans = 0
for r in range(0, R-2):
    for c in range(0, C-2):
        if A[r][c] != B[r][c]:
            do_flip(r, c, A)


if is_same(A, B):
    print(ans)
else:
    print(-1)
