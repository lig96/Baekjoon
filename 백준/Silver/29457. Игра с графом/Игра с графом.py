import sys
input = sys.stdin.readline


N, M = map(int, input().split())
# 도시 수, 도로 수
roads = [list(map(int, input().split())) for _ in range(M)]
# 양방향


min_roads = N-1
extra_roads = M - min_roads


if M == 0:
    # 파괴되지 않은 도로 중 1개를 선택 후 패배 여부를 가리는데
    # 그 도로 자체가 없으면 무승부
    print('Draw')
else:
    if extra_roads % 2 == 0:
        print('Alice')
    else:
        print('Bob')