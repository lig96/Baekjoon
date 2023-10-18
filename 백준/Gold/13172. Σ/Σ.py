
import sys
input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def find(b, num):
    # b의 모듈러 곱셈에 대한 역원을 찾는다.
    # b^num를 구한다.
    # 초기 num = X-2

    if num == 1:
        return b

    if num % 2 == 0:
        # 짝수라면
        temp = find(b, num//2) % X
        return temp * temp
    else:
        # 홀수라면
        temp = find(b, num//2) % X
        return temp * temp * find(b, 1)


# 입력
ans = 0
X = 1_000_000_007
M = int(input())
for _ in range(M):
    Ni, Si = map(int, input().split())

# 풀이
    gcd_num = gcd(Si, Ni)
    # temp = (Si * find(Ni, X-2)) % X
    temp = (Si * pow(Ni, X-2, X)) % X
    ans = (ans + temp) % X

# 출력
print(ans)


# frac = []
# for Si, Ni in zip(S, N):
#     # Si, Ni = S[i], N[i]
#     gcd_num = gcd(Si, Ni)
#     Si, Ni = Si//gcd_num, Ni//gcd_num
#     # temp = (Si * find(Ni, X-2)) % X
#     temp = (Si * pow(Ni, X-2, X)) % X
#     frac.append(temp)


# ans = 0
# for i in range(M):
#     ans = (ans + frac[i]) % X
# print(ans)
