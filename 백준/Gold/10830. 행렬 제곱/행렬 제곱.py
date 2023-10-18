

N, B = map(int, input().split())
mat = [x for x in (list(map(int, input().split())) for _ in range(N))]


def mat_calc(mat1, mat2):
    new_mat = [[None for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            temp = sum([(mat1[r][k] * mat2[k][c]) % 1000 for k in range(N)])
            new_mat[r][c] = temp % 1000
    return new_mat


def rec(mat, power):
    if power == 1:
        eye = [[1 if row == col else 0 for col in range(N)]
               for row in range(N)]
        return mat_calc(mat, eye)
    if power % 2 == 0:
        temp = rec(mat, power//2)
        return mat_calc(temp, temp)
    else:
        # 2^101 = 2^100 * 2
        temp = rec(mat, power-1)
        return mat_calc(temp, mat)


ans = rec(mat, B)


for i in ans:
    print(*i)