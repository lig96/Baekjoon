
import sys
input = sys.stdin.readline


def b_f(start):
    dist = [int(1e9) for _ in range(N+1)]
    dist[start] = 0

    for _ in range(N-1):
        for S, E, T in roads_holes:
            # if dist[S] == int(1e9):
            #     continue
            if dist[E] > dist[S]+T:
                # (기존 start에서 E)
                # (기존 start에서 S) + (S에서 E)
                dist[E] = dist[S]+T
    else:
        for S, E, T in roads_holes:
            # if dist[S] == int(1e9):
            #     continue
            if dist[E] > dist[S]+T:
                dist[E] = dist[S]+T
                return True  # 1번이라도 갱신되면
    return False


TC = int(input())
for _1 in range(TC):
    N, M, W = map(int, input().split())
    roads_holes = []
    for _2 in range(M):
        S, E, T = map(int, input().split())
        roads_holes.append((S, E, T))
        roads_holes.append((E, S, T))
    for _3 in range(W):
        S, E, T = map(int, input().split())
        roads_holes.append((S, E, -T))

    ans = b_f(1)

    if ans:
        print('YES')
    else:
        print('NO')
