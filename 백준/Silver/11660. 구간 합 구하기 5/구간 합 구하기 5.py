import sys
input = sys.stdin.readline
print = sys.stdout.write


N, M = map(int, input().split())
mat = []
mat.append([0 for _ in range(N+1)])
for _ in range(N):
    temp = [0] + list(map(int, input().split()))
    mat.append(temp)
# 의도치 않은 -1 인덱싱을 방지하기 위해 여분의 0을 추가해준다.


for r in range(1, N+1):
    for c in range(1, N+1):
        # 0을 추가했기 때문에 N+1이다.
        mat[r][c] = mat[r][c-1] + mat[r-1][c] - mat[r-1][c-1] + mat[r][c]
# 누적합을 만든다.


for _ in range(M):
    x1, y1, x2, y2 = list(map(int, input().split()))

    total = mat[x2][y2]
    lefttop = mat[x1-1][y1-1]
    leftbottom = mat[x2][y1-1]
    righttop = mat[x1-1][y2]

    ans = total - leftbottom - righttop + lefttop
    print(str(ans)+'\n')