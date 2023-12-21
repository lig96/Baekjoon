import copy
import sys
input = sys.stdin.readline


def push_botton(arr, x):
    # 객체 참조에 의한 호출
    for i in range(3):
        nx = x+dx[i]
        if 0 <= nx < N:
            arr[nx] = not arr[nx]
    return


N = int(input())
arr = list(map(lambda x: True if x == '0' else False, input().rstrip()))
target = list(map(lambda x: True if x == '0' else False, input().rstrip()))


dx = [-1, 0, 1]


ans = float('inf')
for first_botton in [False, True]:
    temp_arr = copy.deepcopy(arr)
    cnt = 0

    for x in [0]:
        if first_botton:
            # 0번째 버튼을 누른다면 누름
            push_botton(temp_arr, x)
            cnt += 1

    for x in range(1, N):
        if temp_arr[x-1] != target[x-1]:
            # 바로 직전 배열과 타겟이 다르다면 누름
            # 다음 x로 넘어가면 건들 수 없음
            push_botton(temp_arr, x)
            cnt += 1

    if temp_arr[-1] == target[-1]:
        # 맨 오른쪽이 같을지는 미지수이고
        # 그것보다 왼쪽은 언제나 동일함
        ans = min(ans, cnt)


if ans == float('inf'):
    print(-1)
else:
    print(ans)
