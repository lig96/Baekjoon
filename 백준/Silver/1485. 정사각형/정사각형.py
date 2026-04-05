from itertools import combinations
import sys
input = sys.stdin.readline


def sol(points):
    def dist2(point1, point2):
        a, b = point1
        c, d = point2
        return (a-c)**2 + (b-d)**2

    dist2_list = [dist2(p1, p2) for p1, p2 in combinations(points, 2)]
    dist2_list.sort()

    v0 = dist2_list[0]
    # 첫 4개는 1, 나머지 2개는 root2
    if dist2_list == [v0]*4 + [v0*2]*2:
        return 1
    return 0


for _ in range(int(input())):
    points = [tuple(map(int, input().split())) for _ in range(4)]

    print(sol(points))
