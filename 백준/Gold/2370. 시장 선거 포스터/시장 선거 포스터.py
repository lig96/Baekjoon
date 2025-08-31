import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4)+20)


def sol_greedy():
    def change_covered(l, r):
        ''' coverd에 (l, r)을 추가하되
        기존 좌표와 겹치거나 맞닿는 부분이 있다면 서로 이어붙이고
        기존 좌표는 삭제한다.'''
        start, end = l, r
        for cl, cr in reversed(covered[::]):
            if end < cl-1 or start > cr+1:
                continue
            start = min(cl, start)
            end = max(cr, end)
            covered.remove((cl, cr))
        covered.append((start, end))
        return
    covered = []
    cnt = 0
    for l, r in reversed(posters):
        for cl, cr in covered:
            if cl <= l and r <= cr:
                # 단 한 번이라도 완벽히 가려진다면
                break
            else:
                # covered 내의 좌표들은 서로 맞닿지 않으니
                # 2개 이상의 포스터에 의해 완벽하게 가려질 일은 무조건 없다.
                pass
        else:
            cnt += 1
            change_covered(l, r)
    return cnt


def sol_segtree():
    raise NotImplementedError
    return


def sol_heap():
    raise NotImplementedError
    return


def sol_naive():
    board = [None for _ in range(max_after+1)]
    for i, (l, r) in enumerate(posters_after):
        board[l:r+1] = [i for _ in range(r+1-l)]
    print(board)
    return len(set(board) - set([None]))


def sol_unionfind():
    def union(a, b):
        a, b = find(a), find(b)
        parent[a] = b
        return

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    parent = [i for i in range(max_after+1+1)]
    # 자기 자신이라면 색칠이 안 된 것,
    # 자기 자신이 아니라면 그 다음으로 색칠이 안 된 것을 가리킨다.
    cnt = 0
    for l, r in reversed(posters_after):
        flag = False
        while (now := find(l)) <= r:
            flag = True
            union(now, now+1)
        if flag:
            cnt += 1
    return cnt


n = int(input())
posters = [list(map(int, input().split())) for _ in range(n)]


coordinates = set()
for l, r in posters:
    coordinates.add(l)
    coordinates.add(r)
coordinates = sorted(coordinates)
dic_before2after = {}
# dic_after2before = {}
for i, v in enumerate(coordinates):
    dic_before2after[v] = i
    # dic_after2before[i] = v


posters_after = [(dic_before2after[l], dic_before2after[r])
                 for l, r in posters]
max_after = len(dic_before2after)  # max(dic_before2after.values())


# ans = sol_unionfind()
# ans = sol_naive()
ans = sol_greedy()


print(ans)


'''
입력
3
2 7
6 10
1 3
올바른 정답
3
틀린 정답
2

좌표 압축 안 할 시
 234567
     678910
123

좌표 압축 할 시
1->0
2->1
3->2
6->3
7->4
10->5

 1234
   345
012

4, 5가 압축 과정에서 사라져버린다.
좌표 압축으로 푸는 풀이는 아마 전부 틀린 것 같다.
'''
