N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))


def rec(before, ans):
    if len(ans) == M:
        ans_str = ' '.join(ans)
        if ans_str not in ans_set:
            print(ans_str)
            ans_set.add(ans_str)
        return
    for i in range(before, N):
        rec(i, ans+[str(arr[i])])


ans_set = set()
rec(0, [])
