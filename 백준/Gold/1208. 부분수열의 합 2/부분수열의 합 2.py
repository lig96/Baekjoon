from collections import defaultdict


def rec(dict, arr, i, now_sum):
    if i == len(arr):
        dict[now_sum] += 1
        return
    else:
        rec(dict, arr, i+1, now_sum+arr[i])
        rec(dict, arr, i+1, now_sum)
        return


N, S = map(int, input().split())
arr = list(map(int, input().split()))


left, right = arr[:N//2], arr[N//2:]
left_sum, right_sum = defaultdict(int), defaultdict(int)
rec(left_sum, left, 0, 0), rec(right_sum, right, 0, 0)
left_sum[0] -= 1  # 전부 선택 안 한 공집합으로 깊이 끝까지 간 경우
right_sum[0] -= 1


ans = 0
for l_key in left_sum.keys():
    ans += left_sum[l_key] * right_sum[S-l_key]
# 0이 2가지, S가 3가지 -> 6가지
ans += left_sum[S]
ans += right_sum[S]
# 0을 사용 안 하고, S가 3가지 -> 3가지


print(ans)
