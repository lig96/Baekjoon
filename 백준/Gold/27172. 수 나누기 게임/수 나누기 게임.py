# xi의 모든 약수와 xj를 결투시키는 것과
# xi의 모든 배수와 xj를 결투시키는 것이
# 동일하다고 생각했지만 시간복잡도가 꽤 차이난다.


import sys
input = sys.stdin.readline


N = int(input())
xs = list(map(int, input().split()))


max_x = max(xs)
ans = ['False' for _ in range(max_x+1)]
for x in xs:
    ans[x] = 0


for x in sorted(xs):
    # 경우의 수
    # summation(1_000_000/n) varying n from 1 to 1_000_000
    # 1e7
    for multiple in range(x*2, max_x+1, x):
        if ans[multiple] != 'False':
            ans[multiple] -= 1
            ans[x] += 1

    # # 경우의 수
    # # summation(root(n)) varying n from 1 to 1_000_000
    # # 7e8
    # for divisor_l in range(1, int(x**(1/2))+1):
    #     if x % divisor_l == 0:
    #         if ans[divisor_l] != 'False':
    #             ans[divisor_l] += 1
    #             ans[x] -= 1
    #         divisor_r = x//divisor_l
    #         if (ans[divisor_r] != 'False') and (divisor_r != divisor_l):
    #             # 오른쪽 약수이면서 제곱근이 아닌 수
    #             ans[divisor_r] += 1
    #             ans[x] -= 1


for x in xs:
    sys.stdout.write(str(ans[x])+' ')
