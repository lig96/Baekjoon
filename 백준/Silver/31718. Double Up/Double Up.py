from collections import defaultdict
import sys
input = sys.stdin.readline


def factorize(v):
    '''
    v = 2^a * 3^b * 5^c * ... 형태일 때
    factor = 3^b * 5^c * ... 형태의 수를 반환한다.
    '''
    while v % 256 == 0:
        v //= 256
    while v % 2 == 0:
        v //= 2
    return v


N = int(input())
arr = list(map(int, input().split()))


dict_ = defaultdict(lambda: 0)
for v in arr:
    factor = factorize(v)
    dict_[factor] += 1


print(max(dict_.values()))
