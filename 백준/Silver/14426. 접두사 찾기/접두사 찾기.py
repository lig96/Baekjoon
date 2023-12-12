from bisect import bisect_left
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
S = [input().rstrip() for _ in range(N)]
prefix_arr = [input().rstrip() for _ in range(M)]


S.sort()


ans = 0
for prefix in prefix_arr:
    ind = bisect_left(S, prefix)
    if ind == len(S):
        # 맨 오른쪽에 새로 넣어야 하는 경우
        continue
    string = S[ind]
    if string.startswith(prefix):
        ans += 1


print(ans)
