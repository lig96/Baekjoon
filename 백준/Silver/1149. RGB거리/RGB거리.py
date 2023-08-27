import sys
input = sys.stdin.readline


N = int(input())
mat = []
mat.append(list(map(int, input().split())))


for i in range(1, N):
    mat.append(list(map(int, input().split())))

    a, b, c = mat[i-1]
    mat[i][0] += min(b, c)
    mat[i][1] += min(a, c)
    mat[i][2] += min(a, b)

print(min(mat[-1]))
