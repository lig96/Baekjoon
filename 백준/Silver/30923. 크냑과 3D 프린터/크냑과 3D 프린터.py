N = int(input())
arr = list(map(int, input().split()))


ans = 0
for i in range(0, N-1):
    ans += 2*arr[i]  # 앞면, 뒷면
    ans += 2  # 윗면, 아랫면
    ans += abs(arr[i+1]-arr[i])  # 중간 면
for i in range(N-1, N):
    ans += 2*arr[i]
    ans += 2
ans += arr[0] + arr[-1]  # 맨 왼쪽 면, 맨 오른쪽 면


print(ans)
