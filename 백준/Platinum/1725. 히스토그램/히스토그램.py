import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)+100)


class segTree():
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0 for _ in range(4*len(arr))]
        return

    def build(self):
        def _build(l, r, i):
            if l == r:
                self.tree[i] = (self.arr[l], l)
                return
            mid = (l+r)//2
            _build(l, mid, i*2)
            _build(mid+1, r, i*2+1)
            self.tree[i] = min(self.tree[i*2], self.tree[i*2+1])
            return
        _build(0, len(self.arr)-1, 1)
        return

    def query(self, arr_l, arr_r, i, query_l, query_r):
        if arr_r < query_l or query_r < arr_l:
            return (float('inf'), None)
        if query_l <= arr_l and arr_r <= query_r:
            return self.tree[i]
        mid = (arr_l+arr_r)//2
        left_ret = self.query(arr_l, mid, i*2, query_l, query_r)
        right_ret = self.query(mid+1, arr_r, i*2+1, query_l, query_r)
        return min(left_ret, right_ret)


def rec(l, r):
    if l > r:
        return -float('inf')
    if l == r:  # 없어도 됨. 위에서 걸러짐.
        return 1*numbers[l]

    mid = segtree.query(0, len(segtree.arr)-1, 1, l, r)
    mid_ans = (r-l+1) * mid[0]

    left_ans = rec(l, mid[1]-1)
    right_ans = rec(mid[1]+1, r)
    return max(mid_ans, left_ans, right_ans)


N = int(input())
numbers = [int(input()) for _ in range(N)]


segtree = segTree(numbers)
segtree.build()


ans = rec(0, N-1)


print(ans)
