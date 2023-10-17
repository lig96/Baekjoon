import sys
print = sys.stdout.write


def rec(row, col, width):
    for r in range(row+width, row+2*width):
        for c in range(col+width, col+2*width):
            graph[r][c] = ' '

    if width == 1:
        return
    else:
        for i in [0, 1, 2, 3, 5, 6, 7, 8]:
            row_new = row + width * (i//3)
            col_new = col + width * (i % 3)
            rec(row_new, col_new, width//3)
            # 012
            # 345
            # 678


N = int(input())


graph = [['*' for _ in range(N)] for _ in range(N)]


rec(0, 0, N//3)


for i in graph:
    print(''.join(i)+'\n')
