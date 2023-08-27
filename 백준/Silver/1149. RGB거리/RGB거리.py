import sys
input = sys.stdin.readline


N = int(input())
mat = []
for i in range(N):
    temp = list(map(int, input().split()))
    mat.append(temp)


rr, gg, bb = 0, 0, 0
for i in range(1, N):
    mat[i][0] += min(mat[i-1][1], mat[i-1][2])
    mat[i][1] += min(mat[i-1][0], mat[i-1][2])
    mat[i][2] += min(mat[i-1][0], mat[i-1][1])

print(min(mat[-1]))
