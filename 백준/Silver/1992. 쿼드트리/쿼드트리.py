import sys
input = sys.stdin.readline
print = sys.stdout.write


def rec(video):
    if is_all_same(video):
        return video[0][0]

    l = len(video)
    top, bottom = range(0, l//2), range(l//2, l)
    left, right = range(0, l//2), range(l//2, l)
    v1 = [[video[r][c] for c in left] for r in top]
    v2 = [[video[r][c] for c in right] for r in top]
    v3 = [[video[r][c] for c in left] for r in bottom]
    v4 = [[video[r][c] for c in right] for r in bottom]
    # v1 v2
    # v3 v4 형태
    return '('+rec(v1)+rec(v2)+rec(v3)+rec(v4)+')'


def is_all_same(x):
    target = x[0][0]
    for r in range(len(x)):
        for c in range(len(x[0])):
            if x[r][c] != target:
                return False
    return True


N = int(input())
video = [list(input().rstrip()) for _ in range(N)]


ans = rec(video)


print(ans)
