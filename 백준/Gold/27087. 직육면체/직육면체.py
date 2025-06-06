# 세 모서리 중 2개 혹은 3개가 p의 배수라면,
# A=ap, B=bp로 놓고 ap*bp*1로 넓게 놓고 C차원으로 놓으면 된다.
#
# 세 모서리 중 0개가 p의 배수라면,
# 부피, 즉 A*B*C는 p^2(p*p*1의 부피)의 배수일 수가 없으니 놓을 수 없다.
# p가 소수이기 때문에 다른 소인수들의 곱이 p가 될 수는 없다.
#
# 세 모서리 중 1개가 p의 배수라면,
# A=ap^1, B=b, C=c라면 배수가 될 수 없고 놓을 수 없다.
# A=ap^2, B=1, C=1이라면 배수가 될 수 있지만 놓을 수 없다.
# 한편 배수가 될 수 있고 놓을 수 있는 경우의 수가 존재할 가능성도 있다.
# 따라서 이러한 자명하지 않은 경우를 다시 증명해야 한다.
# A, B가 p의 배수가 아니고 C가 p의 배수라 하자.
# 큰 직육면체의 A*B면에 닿는 작은 직육면체의 면의 넓이는 1*p이거나 p*p이다.
# 채울 수 있다면 A*B는 p의 배수여야 한다.
# 하지만 A*B는 p의 배수일 수가 없다.
# 따라서 놓을 수 없다.
#
# 즉 세 모서리 중 2개 혹은 3개가 p의 배수라면 놓을 수 있고 아니라면 놓을 수 없다.


import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    A, B, C, p = map(int, input().split())

    cnt = [(i % p == 0) for i in [A, B, C]].count(True)
    ans = 1 if cnt >= 2 else 0

    print(ans)
