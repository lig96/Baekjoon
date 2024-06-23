import sys
input = sys.stdin.readline
def print(x): return sys.stdout.write(str(x[0])+' '+str(x[1])+'\n')


N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]


points.sort(key=lambda x: (x[1], x[0]))


for point in points:
    print(point)
