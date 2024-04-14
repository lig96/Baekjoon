import sys
input = sys.stdin.readline


vertexes = [list(map(int, input().split())) for _ in range(2047)]


dims = [{} for _ in range(11)]


for vertex in vertexes:
    for i, xi in enumerate(vertex):
        if xi in dims[i]:
            dims[i][xi] += 1
        else:
            dims[i][xi] = 1


for i, dim in enumerate(dims):
    a, b = dim.items()
    print(a[0] if a[1] < b[1] else b[0], end=' ')
    # a[0]이 값, a[1]이 개수
