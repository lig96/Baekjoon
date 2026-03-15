import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def combinations(iterable, r):
    def combinations_(start_i, path):
        if len(path) == r:
            yield path
        else:
            for i in range(start_i, len(iterable)):
                path.append(iterable[i])
                yield from combinations_(i+1, path)
                path.pop()

    yield from combinations_(0, [])


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    n, *arr = map(int, input().split())
    # assert n == len(arr)

    ans = sum(gcd(a, b) for a, b in combinations(arr, 2))

    sys_print(str(ans)+'\n')
