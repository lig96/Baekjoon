import sys
input = sys.stdin.readline


def dfs(r, c, before, cost):
    if r == R:
        return cost

    # 무조건 한 칸씩 내려가니 방문 처리 필요 없음
    cost += mat[r][c]
    ret = float('inf')

    for newc in [-1, 0, 1]:
        if not (0 <= c+newc < C):
            continue
        if before == newc:
            continue
        ret = min(ret, dfs(r+1, c+newc, newc, cost))
    return ret


R, C = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(R)]


ans = float('inf')
for c in range(C):
    ans = min(ans, dfs(0, c, None, 0))


print(ans)
