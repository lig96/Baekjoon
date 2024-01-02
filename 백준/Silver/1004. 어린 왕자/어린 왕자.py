import sys
input = sys.stdin.readline


def find_dist(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)


T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for cx, cy, r in planets:
        is_start_in_p = (find_dist((cx, cy), (x1, y1)) < r)
        is_end_in_p = (find_dist((cx, cy), (x2, y2)) < r)
        # 점이 행성계 안에 속하면 True, 아니면 False
        if is_start_in_p ^ is_end_in_p:
            # 연산자 xor. !=이랑 동일.
            ans += 1

    print(ans)
