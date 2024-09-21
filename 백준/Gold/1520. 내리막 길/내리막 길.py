import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(500*500)+100)


def dfs(r, c, ways):
    if (r, c) == (R-1, C-1):
        visited[r][c] = 1
    else:
        visited[r][c] = 0

    # print((r, c))
    # print(*visited, sep='\n')

    temp = []
    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if not (0 <= newr < R and 0 <= newc < C):
            continue
        if board[r][c] <= board[newr][newc]:
            continue

        # print((newr, newc, visited[r][c]))

        if visited[newr][newc] == -1:
            temp.append(dfs(newr, newc, ways))
        else:
            temp.append(visited[newr][newc])
    visited[r][c] += sum(temp)

    # if (r, c) == (0, 0):
    #     print((newr, newc, visited[r][c]), 'hi')
    # print(*visited, sep='\n')

    return visited[r][c]


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
# print(*board, sep='\n')


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


visited = [[-1 for _ in range(C)] for _ in range(R)]
dfs(0, 0, 1)


# print()
print(visited[0][0])
# print(*visited, sep='\n')

# [1, 1, 1, 2, 1]
# [1, -1, -1, 1, 1]
# [1, -1, -1, 1, -1]
# [1, 1, 2, 1, 1]
