def sol(N):
    ret = None
    if N % 2 == 0:
        # 짝수
        ret = 1  # 후공
    else:
        # 홀수
        ret = 0  # 선공
    return ret


N = int(input())


print("SK" if sol(N) == 0 else "CY")
