
import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
arr = list(map(int, input().split()))


dp = [(1, i) for i in range(N)]
for last in range(1, N):
    for prev in range(0, last):
        if arr[prev] < arr[last]:
            if dp[last][0] < dp[prev][0]+1:
                dp[last] = (dp[prev][0]+1, prev)


ind = -1
ans_1 = -1
for i, (v, _) in enumerate(dp):
    if ans_1 < v:
        ind = i
        ans_1 = v
print(str(ans_1))
print('\n')
if ans_1 == N:
    for v in arr:
        print(str(v)+' ')
else:
    ans_2 = []
    while True:
        ans_2.append(arr[ind])
        if ind == dp[ind][1]:
            break
        else:
            ind = dp[ind][1]
    for v in ans_2[::-1]:
        print(str(v)+' ')
