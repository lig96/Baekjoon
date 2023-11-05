N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy.append(xy[0])


ans = 0
for i in range(N):  # 현재 len(xy) = N+1. 1 작게 설정
    x0, y0 = xy[i]
    x1, y1 = xy[i+1]
    ans += x0*y1
    ans -= x1*y0


print(round(abs(ans)/2, 1))
