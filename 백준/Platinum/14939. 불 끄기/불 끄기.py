# https://technicolour.tistory.com/19


import copy


def push_botton(graph, r, c):
    # 객체 참조에 의한 호출
    for i in range(5):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < 10 and 0 <= nc < 10:
            graph[nr][nc] = not graph[nr][nc]
    return


graph = [[False for _ in range(10)] for _ in range(10)]
for r in range(10):
    for c, v in enumerate(input()):
        if v == 'O':
            graph[r][c] = True


dr, dc = [0, 0, 1, -1, 0], [1, -1, 0, 0, 0]


ans = float('inf')
for bottons in range(1 << 10):  # 2^10, 1024
    temp_graph = copy.deepcopy(graph)
    cnt = 0

    for r in [0]:
        for c in range(10):
            newc = -1*c+9
            # 위치, c, newc
            # 맨 왼쪽, 0, 9
            # 맨 오른쪽, 9, 0
            # c는 맨 왼쪽이 0이지만
            # 비트마스킹은 맨 오른쪽이 0임
            # 이렇게 안 해도 좌우반전을 한 뒤에
            # 비트마스킹을 하겠다는 뜻이라 오류는 안 남
            if bottons & (1 << newc):
                # c번째 버튼이 1이라면 버튼을 누름
                push_botton(temp_graph, r, c)
                cnt += 1

    for r in range(1, 10):
        for c in range(10):
            if temp_graph[r-1][c]:
                # 바로 윗 열의 temp_graph의 c가 켜져있다면
                # 무조건 현재 열에서 버튼을 눌러서 꺼야 함
                # 열이 다음으로 넘어가면 건들 방법이 없음
                push_botton(temp_graph, r, c)
                cnt += 1

    if not any(temp_graph[-1]):
        # 윗 열, 그 윗 열의 윗 열, ~~~은 무조건 꺼져있고
        # 자기 자신이 꺼져있다면
        ans = min(ans, cnt)


if ans == float('inf'):
    print(-1)
else:
    print(ans)
