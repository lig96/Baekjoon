import sys
input = sys.stdin.readline


N: str = input().rstrip()


N: list[int] = sorted(map(int, list(N)), reverse=True)
if N[-1] == 0 and sum(N) % 3 == 0:
    ans = "".join(map(str, N))
else:
    ans = "-1"


print(ans)
