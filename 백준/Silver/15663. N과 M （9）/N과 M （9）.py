N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))


def rec(before, ans, level):
    if level == (M+1):
        if ' '.join(ans) not in set_:
            print(' '.join(ans))
            set_.add(' '.join(ans))
        return
    for i in range(N):
        if i not in before:
            rec(before+[i], ans+[str(arr[i])], level+1)


set_ = set()
rec([], [], 1)