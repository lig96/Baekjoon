N, K = map(int, input().split())
A_arr = list(map(int, input().split()))


first_element = A_arr[0]
ans = 0
for i, A in enumerate(A_arr):
    diff = (first_element + K*i) - A
    if diff >= 0:
        ans += diff
    else:
        ans += (-diff * i)
        first_element += -diff


print(ans)
