# T = A_sum[i] + B_sum[j] 를 만족시키는 i, j를 찾으면 된다.
# 여기서 A_sum이 1차원이라면 i도 1차원이고, 2차원이라면 2차원이다.

# 방법 1.
# T = (1+4), (2+3), (3+2), (4+1) 순회를 돌며
# A_sum == T_tuple[0], B_sum == T_tuple[1]이 되는
# 개수를 찾아 서로 곱한 뒤 더한다.
# 방법 2.
# A_sum 순회를 돌며
# (T-A_sum) == B_sum이 되는
# 개수를 찾아 곱하지 않고 더한다.

# 방법 a.
# 누적합 배열을 정렬 후 이분탐색 2번을 통해 target 개수를 찾는다.
# 방법 b.
# 누적합 배열을 dict, Counter 변환 후 인덱싱을 통해 target 개수를 찾는다.


from collections import Counter
import bisect
import sys
input = sys.stdin.readline


def make_prefix_sum(arr):
    temp_sum = []
    for s in range(0, len(arr)):
        temp = arr[s]
        temp_sum.append(temp)
        for e in range(s+1, len(arr)):
            temp += arr[e]
            temp_sum.append(temp)
    return temp_sum


T = int(input())
n = int(input())
A_arr = list(map(int, input().split()))
m = int(input())
B_arr = list(map(int, input().split()))


A_sum = make_prefix_sum(A_arr)  # O(n^2)
B_sum = make_prefix_sum(B_arr)  # O(m^2)
# B_arr = [1, 3, 2]
# B_sum = [#1, 4, 6, #3, 5, #2]
# 2차원 행렬이 아니라 1차원으로 되어있음
# B_sum[0] = 0 포함 ~ 0 포함
# B_sum[1] = 0 포함 ~ 1 포함
# ~~~
# B_sum[4] = 1 포함 ~ 2 포함


A_sum.sort()  # O(nlogn)
# B_sum.sort()  # O(mlogm)
B_Counter = Counter(B_sum)
cnt = 0
before = 'default'
for i in range(len(A_sum)):  # O(n^2)
    if A_sum[i] == before:
        cnt += temp
    else:
        before = A_sum[i]
        target = T-A_sum[i]
        if False:  # 방법 a.
            left = bisect.bisect_left(B_sum, target)  # O(logm)
            right = bisect.bisect_right(B_sum, target)  # O(logm)
            temp = (right-left)
        else:  # 방법 b.
            temp = B_Counter[target]
        cnt += temp


print(cnt)
