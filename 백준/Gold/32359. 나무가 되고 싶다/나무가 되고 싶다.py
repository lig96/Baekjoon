# 문제에서 요구하는 집합이 유한집합이라면
# 그 크기는 항상 N-1 이하이다.


from collections import deque, defaultdict
import sys
input = sys.stdin.readline


def traverse():
    visited = defaultdict(lambda: False)
    for x in vi:
        visited[x] = True
    arr = deque()

    cnt = 0

    x = 0  # 0은 임시 인덱스. 1부터 V에 포함됐을까봐
    visited[x] = True
    arr.append(x)

    while arr:
        x = arr.popleft()
        if (x > max_vi) or (cnt >= N):
            # dfs일 때, bfs일 때
            return -1
        for nx in [2*x, 2*x+1]:
            if visited[nx]:
                continue
            visited[nx] = True
            arr.append(nx)
            cnt += 1

    return cnt


N = int(input())
vi = list(map(int, input().split()))


max_vi = max(vi)


ans = traverse()


print(ans)
