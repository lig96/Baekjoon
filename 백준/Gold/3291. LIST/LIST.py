N = int(input())
arr = [(input(), input()) for _ in range(N)]


ans_arr = ['' for _ in range(N)]
for i, (name, oper) in enumerate(arr):
    if oper == 'SAME':
        ans_arr[i] = name
for i, (name, oper) in enumerate(arr):
    if oper == 'DOWN':
        for j in range(0, i):
            if not ans_arr[j]:
                ans_arr[j] = name
                break
for i, (name, oper) in enumerate(arr):
    if oper == 'UP':
        for j in range(i+1, N):
            if not ans_arr[j]:
                ans_arr[j] = name
                break


for ans in ans_arr:
    if ans == 'HIGHHOPES':
        print('HGHHOPES')
    else:
        print(ans)
