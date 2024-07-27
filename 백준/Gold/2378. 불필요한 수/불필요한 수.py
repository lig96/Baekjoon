# 1
# 11
# 121
# 1331
# 14641
# 15AA51
# 규칙은 이항계수 혹은 nCr이다
# 손으로 적은 수에 이끌려 파스칼의 삼각형을 구현하면
# 메모리와 시간이 터진다.
# (x+y)^n의 계수는
# 괄호 n개 중에서 x를 i개 택하는 경우의 수,
# 즉 nCi, i=0..n(총 n+1개가 나오는 거 유의)이다.
# 삼각형의 마지막 줄은
# 나이브하게 O(개수*큰수연산, N=1e5일때 3만 자리)으로 구하면 된다.
# 이렇게 나온 계수들을 모두 저장하면 메모리가 터진다.
# 그때그때 불필요한지만 저장하면 된다.
# 모듈러 성질에 따라 x%M==0이면 x는 불필요하다.
# (골3, PyPy3 8001ms)
#
# x%M==0이라는 건
# x의 소인수분해의 지수들이 M의 소인수분해의 지수들보다 크다는 걸 뜻한다.
# x = nCr = n!/(n-r)!/r!이니
# 르장드르의 공식과 소인수분해 알고리즘을 통해
# n!, (n-r)!, r!, M의 소인수분해를 빠르게 하고
# 각 소인수마다 지수의 대소를 비교하면 된다. 아마도.
# (#11439와 동일한 플4, PyPy3 200ms)


import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


N, M = map(int, input().split())


ans_arr = []
# nCr(n=N-1, r=0..N-1)
for r in range(0, (N+1)//2):
    now = now * (N-r) // r if r != 0 else 1
    if now % M == 0:
        ans_arr.append(r+1)  # 원인덱싱
        opposite = N-1-r
        if r != opposite:
            ans_arr.append(opposite+1)
ans_arr.sort()


sys_print(str(len(ans_arr))+'\n')
for v in ans_arr:
    sys_print(str(v)+'\n')
# sys_print('\n'.join(map(str, ans_arr)))
