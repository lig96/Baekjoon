import sys
input = sys.stdin.readline


def dist2(a, b):
    '''
    return squared distance between dot a and b.
    '''
    x1, y1 = a
    x2, y2 = b
    return (x2-x1)**2 + (y2-y1)**2


W, H, X, Y, P = map(int, input().split())
players = [list(map(int, input().split())) for _ in range(P)]


R = H//2
cnt = 0


for x, y in players:
    if not ((X-R <= x <= X+W+R) and (Y <= y <= Y+H)):
        # 링크를 감싸는 가상의 큰 사각형
        continue

    if (X <= x <= X+W) and (Y <= y <= Y+H):
        # 중앙의 사각형
        cnt += 1
    elif dist2((X, Y+R), (x, y)) <= R**2:
        # 왼쪽 원
        cnt += 1
    elif dist2((X+W, Y+R), (x, y)) <= R**2:
        # 왼쪽 원
        cnt += 1


print(cnt)
