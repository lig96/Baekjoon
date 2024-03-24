import sys
input = sys.stdin.readline
print = sys.stdout.write


def make_OPN():
    sieve = [True for _ in range(max_n+1)]
    # sieve[i] = 숫자 i가 소수인지 여부
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(max_n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, max_n+1, i):
                sieve[j] = False

    return [i for i, v in enumerate(sieve[3:], start=3) if v]


def sol(n, arr, set_):
    for i in range(len(arr)):
        a, b = arr[i], n-arr[i]
        if b in set_:
            return f"{n} = {a} + {b}"
    return "Goldbach's conjecture is wrong."


max_T = 100_000
max_n = 1_000_000


arr_OPN = make_OPN()
set_OPN = set(arr_OPN)
# odd_prime_numbers


for _ in range(max_T):
    n = int(input())
    if n == 0:
        break

    ans = sol(n, arr_OPN, set_OPN)

    print(ans+'\n')
