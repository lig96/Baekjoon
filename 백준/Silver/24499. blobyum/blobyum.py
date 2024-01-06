import sys
input = sys.stdin.readline


N, K = map(int, input().split())
pies = list(map(int, input().split()))


temp_sum = sum(pies[0:K])
ans = temp_sum
for s in range(1, N):
    e = (s+K-1) % N
    temp_sum = temp_sum + pies[e] - pies[s-1]
    if ans < temp_sum:
        ans = temp_sum


print(ans)
