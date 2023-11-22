def f(x):
    # 0 이상 x 이하의 정수를
    # 이진수로 변환했을 때
    # 1의 개수
    ans = 0
    for i in range(1, x.bit_length()+1):
        div, mod = divmod(x, 2**i)
        ans += div * 2**(i-1)
        # 온전한 덩어리의 개수 * 온전한 덩어리 속 1의 개수
        if mod < 2**(i-1):
            # 온전하지 않은 덩어리의 첫 0들
            pass
        else:
            ans += mod - 2**(i-1) + 1
            # 온전하지 않은 덩어리의 마지막 1들
    return ans


A, B = map(int, input().split())


print(f(B)-f(A-1))
