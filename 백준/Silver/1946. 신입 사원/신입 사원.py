import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(arr):
    oks = []
    min_rank = N + 1
    for i in arr:
        if i[1] < min_rank:
            oks.append(i)
            min_rank = i[1]
    return len(oks)


T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    # 오름차순 정렬. 즉 뒤에 오는 게 나쁨

    ans = sol(arr)

    print(str(ans)+'\n')
