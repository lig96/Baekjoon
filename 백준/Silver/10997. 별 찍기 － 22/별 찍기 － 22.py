
N = int(input())

if N == 1:
    print('*')
    exit()
elif N == 2:
    print('*****')
    print('*')
    print('* ***')
    print('* * *')
    print('* * *')
    print('*   *')
    print('*****')
    exit()


cols = 1 + 4*(N-1)  # 4 - 13
rows = 7 + 4*(N-2)  # 4 - 15

graph = [[' ' for _ in range(cols)] for _ in range(rows)]


def rec(r, c, c_low, r_low):
    global rows, cols
    flag = False
    while c >= c_low:
        graph[r][c] = '*'
        c -= 1
        flag = True
    else:
        c += 1
        c_low += 2
    # print(*graph, sep='\n')
    # print('one')
    while r < rows:
        graph[r][c] = '*'
        r += 1
        flag = True
    else:
        r -= 1
        rows -= 2
    # print(*graph, sep='\n')
    # print('two')
    while c < cols:
        graph[r][c] = '*'
        c += 1
        flag = True
    else:
        c -= 1
        cols -= 2
    # print(*graph, sep='\n')
    # print('three')
    while r >= r_low:
        graph[r][c] = '*'
        r -= 1
        flag = True
    else:
        r += 1
        r_low += 2
    # print(*graph, sep='\n')
    # print('four')
    if not flag:
        return
    else:
        # print(*graph, sep='\n')
        # print('one loop')
        rec(r, c, c_low, r_low)


rec(0, cols-1, 0, 2)

for i in graph:
    print(''.join(i).rstrip())