from collections import deque
import sys
input = sys.stdin.readline


def children(puzzle):
    ret = []
    zero_pos = puzzle.index('0')
    r, c = zero_pos//3, zero_pos % 3
    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if not (0 <= newr < 3 and 0 <= newc < 3):
            continue
        temp = list(puzzle)
        new_zero_pos = newr*3+newc
        swap(temp, zero_pos, new_zero_pos)
        ret.append(''.join(temp))
    return ret


def swap(pz, a, b):
    pz[a], pz[b] = pz[b], pz[a]
    return


def bfs(startx):
    qu = deque()
    visited = set()
    qu.append((startx, 0))
    visited.add(startx)
    while qu:
        x, depth = qu.popleft()
        for nxt in children(x):
            if nxt not in visited:
                if nxt == ans_str:
                    return depth+1
                qu.append((nxt, depth+1))
                visited.add(nxt)
    return -1


puzzle = ''.join(''.join(input().split()) for _ in range(3))
# 이중리스트가 아니라 flatten된 str 형식


ans_str = "123456780"
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


if puzzle == ans_str:
    ans = 0
else:
    ans = bfs(puzzle)


print(ans)
