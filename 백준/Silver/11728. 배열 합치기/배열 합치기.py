import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


N, M = map(int, input().split())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))


ans_arr = [None for _ in range(N+M)]
l, r = 0, 0
for i in range(N+M):
    if A_arr[l] <= B_arr[r]:
        ans_arr[i] = A_arr[l]
        l += 1
    else:
        ans_arr[i] = B_arr[r]
        r += 1
    if l == N or r == M:
        resumed_i = i
        break
if l == N:
    # A_arr 순회가 끝나고 B_arr가 남았으면
    ans_arr[resumed_i+1:] = B_arr[r:]
else:
    ans_arr[resumed_i+1:] = A_arr[l:]


sys_print(' '.join(map(str, ans_arr)))
