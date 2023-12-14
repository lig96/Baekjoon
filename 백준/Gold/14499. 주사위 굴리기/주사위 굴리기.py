def move_dice(d):
    if order == 1:
        t, e, b, w = d['top'], d['east'], d['bottom'], d['west']
        d['top'], d['east'], d['bottom'], d['west'] = w, t, e, b
    elif order == 2:
        t, e, b, w = d['top'], d['east'], d['bottom'], d['west']
        d['top'], d['east'], d['bottom'], d['west'] = e, b, w, t
    elif order == 3:
        t, n, b, s = d['top'], d['north'], d['bottom'], d['south']
        d['top'], d['north'], d['bottom'], d['south'] = s, t, n, b
    else:
        t, n, b, s = d['top'], d['north'], d['bottom'], d['south']
        d['top'], d['north'], d['bottom'], d['south'] = n, b, s, t
    return d


N, M, r, c, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4


dice = {'top': 0, 'east': 0, 'west': 0,
        'north': 0, 'south': 0, 'bottom': 0}
dr, dc = [None, 0, 0, -1, 1], [None, 1, -1, 0, 0]


for order in orders:
    if not (0 <= r+dr[order] < N and 0 <= c+dc[order] < M):
        continue

    dice = move_dice(dice)
    r, c = r+dr[order], c+dc[order]

    if graph[r][c] == 0:
        graph[r][c] = dice['bottom']
    else:
        dice['bottom'] = graph[r][c]
        graph[r][c] = 0

    print(dice['top'])
