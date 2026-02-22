import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def sol(A, B):
    # 정수 부분 출력
    sys_print(str(A//B))
    sys_print(".")
    # 소수 부분 출력
    for _ in range(1900):
        A = (A % B)*10
        if A == 0:
            return
        sys_print(str(A//B))
    return


A, B = map(int, input().split())


sol(A, B)
