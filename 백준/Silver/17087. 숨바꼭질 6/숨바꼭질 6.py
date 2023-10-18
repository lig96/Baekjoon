import sys
input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
arr = [abs(x-S) for x in arr]


my_gcd = arr[0]
for i in arr:
    my_gcd = gcd(my_gcd, i)


print(my_gcd)