def rec(r, c, r_lower, c_lower, r_upper, c_upper):
    original_r, original_c = r, c

    while c >= c_lower:
        # 왼쪽으로 이동
        graph[r][c] = '*'
        c -= 1
    else:
        c += 1
        c_lower += 2
    while r < r_upper:
        # 아래쪽으로 이동
        graph[r][c] = '*'
        r += 1
    else:
        r -= 1
        r_upper -= 2
    while c < c_upper:
        # 오른쪽으로 이동
        graph[r][c] = '*'
        c += 1
    else:
        c -= 1
        c_upper -= 2
    while r >= r_lower:
        # 위로 이동
        graph[r][c] = '*'
        r -= 1
    else:
        r += 1
        r_lower += 2

    if (original_r, original_c) == (r, c):
        return
    else:
        rec(r, c, r_lower, c_lower, r_upper, c_upper)
        return


N = int(input())


if N == 1:
    print('*')
    exit()
c_upper = 1 + 4*(N-1)
r_upper = 7 + 4*(N-2)
graph = [[' ' for _ in range(c_upper)] for _ in range(r_upper)]


rec(0, c_upper-1, 2, 0, r_upper, c_upper)


for i in graph:
    print(''.join(i).rstrip())
