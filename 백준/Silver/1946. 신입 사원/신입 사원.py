# olds 리스트 대신 cnt=0, cnt += 1을 해도 된다.
# arr.sort() 대신 arr=[0]*N+1, arr[a]=b 식으로 배열을 만들어도 된다.


import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(arr):
    olds = []
    min_rank = N + 1
    for new in arr:
        if new[1] < min_rank:
            olds.append(new)
            min_rank = new[1]
            # [1]이 좋아서 new가 추가되어도
            # 언제나 old는 [0]이 좋기 때문에
            # old를 뺄 필요 없음
    return len(olds)


T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    # 오름차순 정렬. 뒤에 오는 게 언제나 [0]이 나쁨

    ans = sol(arr)

    print(str(ans)+'\n')
