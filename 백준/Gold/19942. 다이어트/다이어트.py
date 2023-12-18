def dfs(depth, pfsvc, temp_ans_arr):
    global ans, ans_arr

    if depth == N:
        if not is_healthy(pfsvc):
            return
        if ans > pfsvc[4]:
            ans = pfsvc[4]
            ans_arr = temp_ans_arr[::]
        elif ans == pfsvc[4]:
            # ans = pfsvc[4]
            if temp_ans_arr < ans_arr:
                ans_arr = temp_ans_arr[::]
        return

    if pfsvc[4] > ans:
        # 끝까지 가지 않더라도 이미 비용이 초과
        return
    # 넣는다.
    for i in range(5):
        pfsvc[i] += foods[depth][i]
    temp_ans_arr.append(depth+1)  # 0인덱싱이 아니라 1인덱싱
    dfs(depth+1, pfsvc, temp_ans_arr)
    for i in range(5):
        pfsvc[i] -= foods[depth][i]
    temp_ans_arr.pop()

    # 안 넣는다.
    dfs(depth+1, pfsvc, temp_ans_arr)

    return


def is_healthy(arr):
    for i in range(4):
        if arr[i] < ms[i]:
            return False
    return True


N = int(input())
ms = list(map(int, input().split()))
foods = [list(map(int, input().split())) for _ in range(N)]
# 0, 1, 2, 3, cost


ans = 500*15+1
ans_arr = [N+2]
dfs(0, [0, 0, 0, 0, 0], [])


if ans == 500*15+1:
    print(-1)
else:
    print(ans)
    print(*ans_arr)
