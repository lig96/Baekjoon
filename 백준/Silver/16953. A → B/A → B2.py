# bfs

from collections import deque
A, B = map(int, input().split())
ans = 1


def bfs(graph, v):
    global ans
    global B

    qu = deque()
    qu.append([])
    qu[-1].append(v)

    while qu:
        arr = qu.popleft()

        ans += 1
        qu.append([])
        for i in arr:
            for temp in [i*2, i*10+1]:
                if temp == B:
                    return
                elif temp > B:
                    pass
                elif temp < B:
                    qu[-1].append(temp)
        if qu[-1] == []:
            qu.pop()
            ans = -1


bfs(None, A)

print(ans)
