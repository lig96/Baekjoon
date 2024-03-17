import sys
input = sys.stdin.readline
print = sys.stdout.write


def rec(arr, r, start_i):
    if r == 0:
        yield tuple()
    else:
        for i in range(start_i, N):
            yield from ((arr[i],)+x for x in rec(arr, r-1, i+1))


N, M = map(int, input().split())
numbers = list(map(int, input().split()))


numbers.sort()


ans = set()
for i in rec(numbers, M, 0):
    ans.add(i)
ans = sorted(ans)


print('\n'.join(map(lambda i: ' '.join(map(str, i)), ans)))
# for i in ans:
#     temp = ' '.join(map(str, i))
#     print(temp+'\n')
# 동일
