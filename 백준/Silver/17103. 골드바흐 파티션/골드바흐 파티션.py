import sys
input = sys.stdin.readline
print = sys.stdout.write


def make_PN():
    sieve = [True for _ in range(max_n+1)]
    # sieve[i] = 숫자 i가 소수인지 여부
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(max_n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, max_n+1, i):
                sieve[j] = False

    return [i for i, v in enumerate(sieve) if v]


def sol(n, arr, set_):
    ret = 0
    for i in range(len(arr)):
        a, b = arr[i], n-arr[i]
        if a > b:
            break
        if b in set_:
            ret += 1
    return ret


T = int(input())
max_n = 1_000_000


arr_PN = make_PN()
set_PN = set(arr_PN)
# prime_numbers


for _ in range(T):
    n = int(input())

    ans = sol(n, arr_PN, set_PN)

    print(str(ans)+'\n')
