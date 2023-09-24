# DFS
# 파이썬, pypy에서 DFS, BFS는 최적화와 관계없이 시간 초과가 나는 듯하다.
# 된다고 하는 블로그의 풀이는 테스트 케이스가 추가된 현재 다시 입력해보면 시간 초과가 난다.
# 동일 정점을 다른 과거로 여러 번 방문하는 것이 가능하기 때문에 visit 처리는 하지 않는다.
# 동일 정점에서부터 미래는 동일하기 때문에 저장이 가능하지만 이 방식은 DP이다.


N = int(input())
mat = [row for row in (list(map(int, input().split())) for _ in range(N))]


def end(r, c, d):
    if d == 0:
        return (N, N) == (r, c+1)
    elif d == 1:
        return (N, N) == (r+1, c)
    elif d == 2:
        return (N, N) == (r+1, c+1)


def wall(r, c, d):
    if d == 0:
        arr = [(r, c), (r, c+1)]
    elif d == 1:
        arr = [(r, c), (r+1, c)]
    elif d == 2:
        arr = [(r, c), (r, c+1), (r+1, c), (r+1, c+1)]

    for testr, testc in arr:
        if mat[testr-1][testc-1] == 1:
            # r, c는 1부터 시작하지만 인덱스는 0부터 시작
            return True
    else:
        return False


def dfs(r, c, dir):
    global ans

    nowr, nowc, nowd = r, c, dir
    for dr, dc, dd in dir_arr[nowd]:
        nr = nowr + dr
        nc = nowc + dc
        nd = nowd + dd

        try:
            if wall(nr, nc, nd):
                # 안쪽에서 1을 만난다면
                continue
        except:
            # 바깥쪽으로 충돌한다면
            continue

        if end(nr, nc, nd):
            ans += 1
            continue
        else:
            dfs(nr, nc, nd)


ans = 0
dir_arr = [
    [(0, 1, 0), (0, 1, 2)],
    [(1, 0, 0), (1, 0, 1)],
    [(1, 1, -2), (1, 1, -1), (1, 1, 0)]
]
dfs(1, 1, dir=0)
# 0가로 -> 가로, 대각선
# 1세로 -> 세로, 대각선
# 2대각선 -> 가로, 세로, 대각선
print(ans)
