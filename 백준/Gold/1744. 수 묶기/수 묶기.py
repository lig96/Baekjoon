import sys
input = sys.stdin.readline


def sol(N, arr):
    arr.sort()
    tied = []
    untied = []

    ind_0 = 0
    while ind_0 < len(arr) and arr[ind_0] <= 0:
        ind_0 += 1
    arr_neg = list(reversed(arr[:ind_0]))  # 내림차순, 0 포함
    arr_pos = arr[ind_0:]  # 오름차순

    while len(arr_pos) >= 2:
        top1 = arr_pos.pop()
        top2 = arr_pos.pop()
        if top2 > 1:
            # 0, 1이라면 그냥 합하는 게 더 크다.
            tied.append(top1*top2)
        else:
            untied.append(top2)
            untied.append(top1)
    while len(arr_neg) >= 2:
        top1 = arr_neg.pop()
        top2 = arr_neg.pop()
        if True:
            tied.append(top1*top2)
    assert len(arr_neg) <= 1 and len(arr_pos) <= 1

    ret = sum(tied) + sum(untied) + sum(arr_neg) + sum(arr_pos)
    return ret


N = int(input())
arr = [int(input()) for _ in range(N)]


ans = sol(N, arr)


print(ans)
