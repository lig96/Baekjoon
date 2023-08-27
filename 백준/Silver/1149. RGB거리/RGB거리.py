import sys
input = sys.stdin.readline


N = int(input())
mat = []
for i in range(N):
    temp = list(map(int, input().split()))
    mat.append(temp)


rr, gg, bb = 0, 0, 0
for i in range(len(mat)):
    mat[i] = [x+y for x, y in zip(mat[i], [rr, gg, bb])]
    r, g, b = mat[i]
    if r > g:
        bb = g
    else:
        bb = r
    #
    if g > b:
        rr = b
    else:
        rr = g
    #
    if b > r:
        gg = r
    else:
        gg = b

print(sorted(mat[-1])[0])