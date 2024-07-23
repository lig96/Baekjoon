import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


class segTree():
    def __init__(self, arr):
        self.arr = arr
        self.leng = len(self.arr)
        self.tree = [0 for _ in range(4*self.leng)]
        self.lazy = [0 for _ in range(4*self.leng)]
        return

    def build(self, arr_l, arr_r, i):
        if arr_l == arr_r:
            self.tree[i] = self.arr[arr_l]
            return
        mid = (arr_l + arr_r) // 2
        self.build(arr_l, mid, i*2)
        self.build(mid+1, arr_r, i*2+1)
        self.tree[i] = sum([self.tree[i*2], self.tree[i*2+1]])
        # 아마 불필요
        return

    def update(self, arr_l, arr_r, i, query_l, query_r, diff):
        self.push(arr_l, arr_r, i)
        if arr_r < query_l or query_r < arr_l:
            return
        if query_l <= arr_l and arr_r <= query_r:
            self.lazy[i] += diff
            self.push(arr_l, arr_r, i)
            return
        mid = (arr_l + arr_r) // 2
        self.update(arr_l, mid, i*2, query_l, query_r, diff)
        self.update(mid+1, arr_r, i*2+1, query_l, query_r, diff)
        self.tree[i] = sum([self.tree[i*2], self.tree[i*2+1]])
        # 아마 불필요
        return

    def push(self, arr_l, arr_r, i):
        if self.lazy[i] != 0:
            self.tree[i] += (arr_r-arr_l+1) * self.lazy[i]
            if arr_l != arr_r:
                self.lazy[i*2] += self.lazy[i]
                self.lazy[i*2+1] += self.lazy[i]
            self.lazy[i] = 0
            return
        return

    def query(self, arr_l, arr_r, i, query_l, query_r):
        self.push(arr_l, arr_r, i)
        if arr_r < query_l or query_r < arr_l:
            return 0
        if query_l <= arr_l and arr_r <= query_r:
            return self.tree[i]
        mid = (arr_l + arr_r) // 2
        lsum = self.query(arr_l, mid, i*2, query_l, query_r)
        rsum = self.query(mid+1, arr_r, i*2+1, query_l, query_r)
        # 아마 필요할 듯
        return sum([lsum, rsum])


N = int(input())
Aarr = list(map(int, input().split()))
M = int(input())
queries = [list(map(int, input().split())) for _ in range(M)]


segtree = segTree(Aarr)
segtree.build(0, segtree.leng-1, 1)


ans_arr = []
for oper, *query in queries:
    if oper == 1:
        i, j, k = query
        segtree.update(0, segtree.leng-1, 1, i-1, j-1, k)
    else:
        x, = query
        ans = segtree.query(0, segtree.leng-1, 1, x-1, x-1)
        ans_arr.append(ans)


sys_print('\n'.join(map(str, ans_arr)))
