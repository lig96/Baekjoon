N = int(input())
arr = [(input(), input()) for _ in range(N)]


ans_arr = ['' for _ in range(N)]
for i, (name, oper) in enumerate(arr):
    # same이면 그대로 넣기
    if oper == 'SAME':
        ans_arr[i] = name
for i, (name, oper) in enumerate(arr):
    # down이면 정방향으로 순회하며 맨 왼쪽에 넣기
    if oper == 'DOWN':
        for j in range(0, i):
            if not ans_arr[j]:
                ans_arr[j] = name
                break
for i, (name, oper) in list(enumerate(arr))[::-1]:
    # up이면 역방향으로 순회하며 맨 오른쪽에 넣기
    if oper == 'UP':
        for j in range(i+1, N)[::-1]:
            if not ans_arr[j]:
                ans_arr[j] = name
                break
# same이 맨 앞이라면 down과 up은 순서 상관 없음


for ans in ans_arr:
    if ans == 'HIGHHOPES':
        print('HGHHOPES')
    else:
        print(ans)
