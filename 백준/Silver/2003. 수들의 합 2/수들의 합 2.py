import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))


presum = [0]
temp = 0  # 덧셈의 역원
for v in arr:
    temp += v
    presum.append(temp)
# sum(arr[start:end]) = presum[end] - presum[start]


s, e = 0, 0
ans = 0
while s <= e < len(presum):
    temp = presum[e] - presum[s]
    if temp == M:
        ans += 1
        s += 1
    elif temp < M:
        e += 1
    else:
        s += 1


print(ans)
