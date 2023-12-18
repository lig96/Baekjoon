# 명시적으로 ans_arr의 대소 조건을 구현하였다.
# '넣는다', '안 넣는다'의 순서에 따라 암묵적으로 구현하면
# 다양한 경우에서 오류가 난다.


def dfs(depth, pfsvc, temp_ans_arr):
    global ans, ans_arr

    if depth == N:
        if not is_healthy(pfsvc):
            return
        if ans > pfsvc[4]:
            # ans가 갱신된다면 무조건 ans_arr가 갱신됨
            ans = pfsvc[4]
            ans_arr = temp_ans_arr[::]
        elif ans == pfsvc[4]:  # 라인 A
            # ans가 동일하다면 특정 조건에서 ans_arr가 갱신됨
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
        if arr[i] < minimums[i]:
            return False
    return True


N = int(input())
minimums = list(map(int, input().split()))
foods = [list(map(int, input().split())) for _ in range(N)]
# 0, 1, 2, 3, cost


ans = int(1e9)
ans_arr = []
# 초기값인 상태로 라인 A에 들어가지 않으니 큰 값 안 넣어도 됨
dfs(0, [0, 0, 0, 0, 0], [])


if ans == int(1e9):
    print(-1)
else:
    print(ans)
    print(*ans_arr)
