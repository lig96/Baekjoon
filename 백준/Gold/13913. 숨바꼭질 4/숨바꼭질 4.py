
from collections import deque
import sys


def bfs():
    dist[N] = 0
    qu.append(N)

    while qu:
        x = qu.popleft()

        if x == K:
            return x

        for newx in (x-1, x+1, x*2):
            if (0 <= newx <= 100_000) and (dist[newx] == -1):
                dist[newx] = dist[x]+1
                parent[newx] = x
                qu.append(newx)


N, K = map(int, input().split())
dist = [-1 for _ in range(100_000+1)]
parent = [-2 for _ in range(100_000+1)]
qu = deque()


ans = bfs()


print(dist[ans])
# 깊이를 출력한다.
ans_arr = []
for i in range(dist[ans]+1):
    ans_arr.append(ans)
    ans = parent[ans]
sys.stdout.write(' '.join(map(str, ans_arr[::-1])))
# 맨 오른쪽에서 시작해서 부모를 찾고 거꾸로 출력한다.
