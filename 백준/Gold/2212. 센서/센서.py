import sys
input = sys.stdin.readline


def sol(N, K, sensors):
    sensors.sort()

    gap = []
    for i in range(N-1):
        gap.append(sensors[i+1] - sensors[i])
    gap.sort()
    for _ in range(K-1):
        if gap:
            gap.pop()

    return sum(gap)


N = int(input())
K = int(input())
sensors = list(map(int, input().split()))


print(sol(N, K, sensors))
