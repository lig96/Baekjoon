# 주석 처리한 len_left_tree를 만드는 코드의 경우
# 최악의 경우 summation(1~N), 즉 N^2/2가 보장된다.
# 앞부터 반복하면 왼쪽으로 치우쳐졌을 때,
# 뒤부터 반복하면 오른쪽으로 치우쳐졌을 때 최악이다.
# 따라서 O(1) 위해 리스트 혹은 딕셔너리를 써야 한다.
#
# 현재 백준에는 오른쪽으로 치우쳐진 케이스가 없어서
# 뒤부터 반복하는 코드가 생각보다 빠르게 수행된다.
# 앞부터 반복. pypy3 - 16_392ms
# 뒤부터 반복. pypy3 -  3_952ms
# 리스트.      pypy3 -   572ms

import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(int(1e5)+2)


def rec(in_i, post_i):
    if in_i[0] == in_i[1]:
        # 트리의 길이가 0이라면
        # 참고로 언제나 in_i와 post_i의 길이는 같음
        return

    left, right, root = make_lrr(in_i, post_i)

    print(str(root)+' ')
    rec(left[0], left[1])
    rec(right[0], right[1])
    return


def make_lrr(in_i, post_i):
    root = postorder[post_i[1]-1]

    # for i1 in range(in_i[0], in_i[1]):
    #     if inorder[i1] == root:
    #         len_l = i1 - in_i[0]
    #         break
    len_l = vi_arr[root] - in_i[0]

    left = (in_i[0], in_i[0]+len_l), (post_i[0], post_i[0]+len_l)
    right = (in_i[0]+len_l+1, in_i[1]), (post_i[0]+len_l, post_i[1]-1)

    return left, right, root


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


vi_arr = [-1 for _ in range(n+1)]
for i, v in enumerate(inorder):
    vi_arr[v] = i


rec((0, n), (0, n))
