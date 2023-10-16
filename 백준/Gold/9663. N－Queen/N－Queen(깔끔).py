def is_promising(r, c):
    for prev_r, prev_c in enumerate(rows[:r]):
        if prev_r == r:
            # 동일 row
            return False
        if prev_c == c:
            # 동일 col
            return False
        if abs(r-prev_r) == abs(c-prev_c):
            # 동일 대각선
            return False
    return True


def dfs(r):
    global cnt

    if r == N:
        cnt += 1
        return
    for c in range(N):
        if is_promising(r, c):
            rows[r] = c
            dfs(r+1)
            rows[r] = -1


N = int(input())


rows = [-1 for _ in range(N)]
cnt = 0


dfs(0)


print(cnt)
