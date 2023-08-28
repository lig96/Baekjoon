import sys
input = sys.stdin.readline


n = int(input())
mat = []
for _ in range(n):
    temp = list(map(int, input().split()))
    mat.append(temp)


before = [0] # 인덱싱 오류가 안 생기면서 덧셈의 항등원
for arr_i in range(len(mat)):
    arr = mat[arr_i]
    for i in range(len(arr)):
        if i == 0:
            new = arr[i] + before[i]
        elif i == (len(arr)-1):
            new = arr[i] + before[i-1]
        else:
            new = arr[i] + max(before[i], before[i-1])
        arr[i] = new
    before = arr

print(max(mat[-1]))
