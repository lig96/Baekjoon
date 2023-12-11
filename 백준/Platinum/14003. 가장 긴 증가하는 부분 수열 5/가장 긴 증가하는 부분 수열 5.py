from bisect import bisect_left
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol():
    for i in range(0, 1):
        v = arr[i]
        values.append(v)

        indexes.append(i)
        parent[i] = 'first'
    for i in range(1, N):
        v = arr[i]
        if values[-1] < v:
            values.append(v)

            indexes.append(i)
            parent[i] = indexes[-1-1]
        else:
            ind = bisect_left(values, v)
            values[ind] = v

            indexes[ind] = i
            if ind == 0:
                parent[i] = 'first'
            else:
                parent[i] = indexes[ind-1]
    return


def print_ans():
    print(str(len(values))+'\n')

    if len(values) == N:
        for v in arr:
            print(str(v)+' ')
    else:
        ans = []
        ans_ind = indexes[-1]
        while True:
            ans.append(arr[ans_ind])
            if parent[ans_ind] == 'first':
                break
            else:
                ans_ind = parent[ans_ind]
        for v in ans[::-1]:
            print(str(v)+' ')
    return


N = int(input())
arr = list(map(int, input().split()))


parent = ['default' for _ in range(N)]
values = []
indexes = []


sol()


print_ans()
