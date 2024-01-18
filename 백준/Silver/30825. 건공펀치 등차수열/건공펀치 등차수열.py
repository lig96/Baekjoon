N, K = map(int, input().split())
A_arr = list(map(int, input().split()))


first_element = A_arr[0]


ans = 0
for i, A in enumerate(A_arr):
    diff = (first_element + K*i) - (A)
    if diff >= 0:
        ans += diff  # 자기 자신
    else:
        # 자기 자신은 0
        ans += (abs(diff) * i)  # A0~Ai-1, i개
        first_element += abs(diff)  # 초항


print(ans)
