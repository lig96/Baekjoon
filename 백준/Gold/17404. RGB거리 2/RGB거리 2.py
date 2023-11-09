N = int(input())
INF = int(1e9)
mat = []
for _ in range(0, 1):
    r, g, b = list(map(int, input().split()))
    temp = [[r, INF, INF], [INF, g, INF], [INF, INF, b]]
    mat.append(temp)
for _ in range(1, N):
    r, g, b = list(map(int, input().split()))
    temp = [[r, g, b], [r, g, b], [r, g, b]]
    mat.append(temp)
# mat[0]에서는 무조건 r을 선택하게끔
# mat[i][r][g] = i번째는 시작이 r이고 현재 선택이 g


for i in range(1, len(mat)):
    for j, (r, g, b) in enumerate(mat[i-1]):
        mat[i][j][0] += min(g, b)
        mat[i][j][1] += min(r, b)
        mat[i][j][2] += min(r, g)


ans = INF
for s in range(3):
    for e in range(3):
        if s != e and mat[-1][s][e] < ans:
            ans = mat[-1][s][e]
print(ans)
