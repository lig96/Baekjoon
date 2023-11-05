def sol(n):
    if n in dic.keys():
        return dic[n]

    # F[2n] = F[n]*(2*F[n-1]+F[n])
    # F[2n+1] = F[n+1]^2 + F[n]^2
    if n % 2 == 0:
        # 짝수라면
        x = n//2
        ans = sol(x)*(2*sol(x-1)+sol(x))
    else:
        # 홀수라면
        x = n//2
        ans = sol(x+1)**2 + sol(x)**2
    dic[n] = ans % 1_000_000_007
    return dic[n]


n = int(input())


dic = dict()
dic[0] = 0
dic[1] = 1


ans = sol(n)


print(ans)
