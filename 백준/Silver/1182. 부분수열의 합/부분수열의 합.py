# 2^20은 브루트 포스로 풀 수 있지만
# 2^40과 같이 더 클 경우 meet in the middle을 써야 한다.


from collections import defaultdict


def rec(dict, arr, i, now_sum):
    if i == len(arr):
        dict[now_sum] += 1
        return
    rec(dict, arr, i+1, now_sum+arr[i])
    rec(dict, arr, i+1, now_sum)
    return


N, S = map(int, input().split())
arr = list(map(int, input().split()))


dict_sum = defaultdict(int)
rec(dict_sum, arr, 0, 0)
dict_sum[0] -= 1  # 아무것도 선택하지 않은 채로 깊이 끝까지 간 경우


print(dict_sum[S])
