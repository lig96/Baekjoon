import sys
input = sys.stdin.readline
sys_print = sys.stdout.write

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]


ans = [1 for _ in range(N)]
# 초기값은 1
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            ans[i] += 1


sys_print(' '.join(map(str, ans)))
