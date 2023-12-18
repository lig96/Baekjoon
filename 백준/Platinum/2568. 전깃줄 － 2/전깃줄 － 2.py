# N이 클 때 길이와 수열 모두 출력하는 LIS


from bisect import bisect_left
import sys
input = sys.stdin.readline
print = sys.stdout.write


def make_dp():
    dp = []
    lengths = []

    for i in [0]:
        dp.append(arr[i])
        lengths.append(len(dp))
    for i in range(1, N):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
            lengths.append(len(dp))
        else:
            ind = bisect_left(dp, arr[i])
            dp[ind] = arr[i]
            lengths.append(ind+1)

    return dp, lengths


def do_print():
    selections = set()
    target_length = len(dp)

    for i, v in list(enumerate(lengths))[::-1]:
        if v == target_length:
            selections.add(left[i])
            target_length -= 1

    print(str(N-len(selections))+'\n')
    for v in left:
        if v not in selections:
            print(str(v)+'\n')

    return


N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)])
left = [x[0] for x in arr]
arr = [x[1] for x in arr]


dp, lengths = make_dp()


do_print()
