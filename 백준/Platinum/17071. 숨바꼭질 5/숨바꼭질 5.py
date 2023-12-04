from collections import deque


def bfs():
    visited = [[False, False] for _ in range(limit+1)]
    visited[input_N][0 % 2] = True
    # 내가 현재 서있는 지점을
    # 짝수 깊이에서 밟았느냐, 홀수 깊이에서 밟았느냐
    # +1, -1을 하면 현재 자리를 유지할 수 있음
    qu = deque()
    qu.append((input_N, input_K, 0))

    while qu:
        n, k, depth = qu.popleft()

        if (k <= limit) and (visited[k] != [False, False]):
            if visited[k][depth % 2]:
                return depth

        newk = k+depth+1
        newd = depth+1
        for newn in [n-1, n+1, n*2]:
            if not (0 <= newn <= limit):
                continue
            if not (0 <= newk <= limit):
                continue
            if visited[newn][newd % 2]:
                continue
            visited[newn][newd % 2] = True
            qu.append((newn, newk, newd))
    return -1


input_N, input_K = map(int, input().split())
limit = 500_000


print(bfs())
