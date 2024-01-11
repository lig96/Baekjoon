import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split())) + [0]


for i in range(0, N)[::-1]:
    if arr[i] > arr[i+1]:
        arr[i] = arr[i+1]+1


print(sum(arr))
