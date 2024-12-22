import sys
input = sys.stdin.readline


N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]


lines.sort(key=lambda x: x[0])


ans = 0
start, end = lines[0]
for x, y in lines[1:]:
    if end < x:
        ans += end-start
        start, end = x, y
    else:
        # start <= x는 보장됨
        # 즉, start <= x <= end
        end = max(end, y)
else:
    ans += end-start


print(ans)
