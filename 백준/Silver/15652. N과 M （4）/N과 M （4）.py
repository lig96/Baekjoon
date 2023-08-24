# 34
def rec(start, end, ans):
    for i in range(start, end):
        ans = ans + str(i) + ' '
        if len(ans) == (M*2):
            print(ans)
        else:
            rec(i, end, ans)
        ans = ans[:-2]
    return


N, M = map(int, input().split())
arr = list(range(1, N+1))

rec(1, N+1, '')
