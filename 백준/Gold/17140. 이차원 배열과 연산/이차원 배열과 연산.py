from collections import Counter
import sys
input = sys.stdin.readline


def sol(A):
    time = 0
    while not check(A) and time <= 100:
        time += 1
        if len(A) >= len(A[0]):
            A = do_oper(A, "R")
        else:
            A = do_oper(A, "C")
    return (-1 if time == 101 else time)


def check(A):
    try:
        return (A[R][C] == K)
    except IndexError as E:
        # 인덱스가 없다면 False가 정상 동작임.
        return False
    except Exception as E:
        raise Exception


def do_oper(A, oper):
    if oper == "C":
        temp = [x for x in zip(*A)]
    else:
        temp = A

    ret = []
    for arr in temp:
        items = list(Counter(arr).items())
        # dict_items([(v, cnt), (v, cnt), (v, cnt)])
        items.sort(key=lambda x: (x[1], x[0]))
        # 그 다음, 수의 등장 횟수가 커지는 순으로,
        # 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다.
        after_sort = []
        # 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다.
        # 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를
        # 모두 넣으며, 순서는 수가 먼저이다.
        for v in items:
            if v[0] == 0:
                # 수를 정렬할 때 0은 무시해야 한다.
                continue
            after_sort.append(v[0])
            after_sort.append(v[1])
        ret.append(after_sort)
    max_leng = max(map(len, ret))
    ret = [x+[0 for _ in range(max_leng-len(x))] for x in ret]
    # R 연산이 적용된 경우에는 가장 큰 행을 기준으로
    # 모든 행의 크기가 변하고, C 연산이 적용된 경우에는
    # 가장 큰 열을 기준으로 모든 열의 크기가 변한다.
    # 행 또는 열의 크기가 커진 곳에는 0이 채워진다.
    ret = ret[:100]
    # 행 또는 열의 크기가 100을 넘어가는 경우에는
    # 처음 100개를 제외한 나머지는 버린다.

    if oper == "C":
        ret = [x for x in zip(*ret)]
    else:
        ret = ret
    return ret


R, C, K = map(int, input().split())
R, C = R-1, C-1
# 제로 인덱싱
A = [list(map(int, input().split())) for _ in range(3)]


ans = sol(A)


print(ans)
