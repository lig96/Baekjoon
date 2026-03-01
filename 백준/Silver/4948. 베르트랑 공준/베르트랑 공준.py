import sys
input = sys.stdin.readline


def make_sieve():
    end = 123_456*2
    nums = [True for _ in range(end+1)]
    nums[0] = False
    nums[1] = False
    for num in range(2, int(end**0.5)+1):
        if not num:
            continue
        for multiples_of_num in range(num*num, end+1, num):
            if nums[multiples_of_num]:
                nums[multiples_of_num] = False
    return nums


def make_cnt_primes_le(sieve):
    counts = [None for _ in range(len(sieve))]
    counts[0] = 0
    for i in range(1, len(sieve)):
        if sieve[i]:
            counts[i] = counts[i-1] + 1
        else:
            counts[i] = counts[i-1]
    return counts


arr_n = [int(n) for n in sys.stdin.readlines()]
arr_n.pop()


sieve = make_sieve()
cnt_primes_le = make_cnt_primes_le(sieve)


for n in arr_n:
    ans = cnt_primes_le[n*2] - cnt_primes_le[n]
    print(ans)
