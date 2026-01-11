import sys
input = sys.stdin.readline


N = int(input())
scores = [int(input()) for _ in range(N)]


ans = 0
for i in reversed(range(N-1)):
    if scores[i] >= scores[i+1]:
        diff = (scores[i]-scores[i+1])+1
        scores[i] -= diff
        ans += diff


print(ans)
