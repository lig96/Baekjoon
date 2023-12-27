# bisect 라이브러리 참고.
# hi = len(arr)로 구현을 해야 함.
# 반복문에서 arr[mid]와 같이 구현이 되기 때문에,
# arr[hi]을 하면 IndexError가 나니
# mid는 hi를 거치지 않도록 구현이 되어 있음.
# 따라서 mid최댓값은 hi-1. 거꾸로 말하면 hi는 mid최댓값+1.


import sys
input = sys.stdin.readline


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]


houses.sort()
lo = 1  # 원래는 0
hi = houses[-1]-houses[0]+1  # 원래는 len(arr)


while lo < hi:
    mid = (lo+hi)//2

    installed_c = 0
    for i in [0]:
        now = houses[i]
        installed_c += 1
    for i in range(1, N):
        if houses[i] >= now + mid:
            now = houses[i]
            installed_c += 1

    if installed_c > C:
        # 갭을 키워야 함
        lo = mid+1
    elif installed_c == C:
        # 갭을 키워야 함
        # bisect_right니까 이 부분 주의.
        lo = mid+1
    else:
        # 갭을 줄여야 함
        hi = mid


print(lo-1)
# bisect_right
# The return value i is such that all e in a[:i] have e <= x
# 슬라이싱의 우측은 exclusive기 때문에
# arr[smth] <= target을 만족하는 smth 중 최대는 lo-1

# 가상의 arr는 gap(인덱스)의 크기가 증가함에 따라
# cnt(밸류)가 감소하기 때문에 살짝 다름.
