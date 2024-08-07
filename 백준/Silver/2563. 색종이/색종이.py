import sys
input = sys.stdin.readline


cnt = int(input())
smalls = [list(map(int, input().split())) for _ in range(cnt)]
W = 10


paper = [[False for _ in range(101)] for _ in range(101)]


for r, c in smalls:
    for i in range(r, r+W):
        for j in range(c, c+W):
            paper[i][j] = True


print(sum(map(sum, paper)))
