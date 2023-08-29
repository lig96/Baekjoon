# bfs

from collections import deque
A, B = map(int, input().split())


def bfs(A, B):
    qu = deque()
    qu.append((A, 1))

    while qu:
        i, level = qu.popleft()

        for temp in [i*2, i*10+1]:
            if temp == B:
                print(level+1)
                return
            elif temp > B:
                pass
            elif temp < B:
                qu.append((temp, level+1))
    else:
        print(-1)


bfs(A, B)
