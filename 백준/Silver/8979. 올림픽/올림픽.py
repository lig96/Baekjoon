import sys
input = sys.stdin.readline


def bisect_left(arr, target):
    lo, hi = 0, len(arr)

    while lo < hi:
        mid = (lo+hi)//2
        if arr[mid] > target:
            lo = mid+1
        else:
            hi = mid
    return lo


N, K = map(int, input().split())
countries = [0 for _ in range(N)]
for _ in range(N):
    n, *medal_n = list(map(int, input().split()))
    countries[n-1] = medal_n


medal_K = countries[K-1]
countries.sort(reverse=True)  # key 설정 불필요


ans = bisect_left(countries, medal_K)


print(ans+1)
