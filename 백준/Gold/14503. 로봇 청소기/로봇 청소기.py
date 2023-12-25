def rec(r, c, d):
    global cnt

    if graph[r][c] == 0:
        graph[r][c] = 2
        cnt += 1

    if is_near_dirty(r, c):
        for _ in range(4):
            # 4번 내에 라인 A로 진입하는 게 보장됨
            d = turn(d)
            newr, newc = r+dr[d], c+dc[d]
            if graph[newr][newc] == 0:
                rec(newr, newc, d)
                return  # 라인 A
    else:
        newr, newc = r-dr[d], c-dc[d]
        # d는 그대로 쓰되 부호가 마이너스
        if graph[newr][newc] != 1:
            rec(newr, newc, d)
            return
        else:
            return


def is_near_dirty(r, c):
    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if graph[newr][newc] == 0:
            return True
    return False


def turn(d):
    if d == 0:
        return 3
    else:
        return d-1


N, M = map(int, input().split())
r, c, d = map(int, input().split())
# 0인 경우 북쪽, # 1인 경우 동쪽,
# 2인 경우 남쪽, # 3인 경우 서쪽
graph = [list(map(int, input().split())) for _ in range(N)]
# 여러 번 방문할 수 있어서 visited는 필요없음
# 0청소안함, 1벽, 2청소함


dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
cnt = 0
rec(r, c, d)


print(cnt)
