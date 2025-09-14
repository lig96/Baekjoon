import sys
input = sys.stdin.readline


N, M = map(int, input().split())
S = [input().rstrip() for _ in range(N)]
check_strings = [input().rstrip() for _ in range(M)]


S_set = set(S)
cnt = 0
for string in check_strings:
    if string in S_set:
        cnt += 1


print(cnt)
