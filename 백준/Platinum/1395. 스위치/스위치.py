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

    def build(self, l, r, i):
        # 어차피 초기값은 다 0으로 빌드됨
        #
        # if l == r:
        #     self.tree[i] = self.arr[l]
        #     return
        # mid = (l+r)//2
        # self.build(l, mid, i*2)
        # self.build(mid+1, r, i*2+1)
        # self.tree[i] = self.tree[i*2]+self.tree[i*2+1]
        return

    def update(self, l, r, i, s, e, v):
        self.push(l, r, i)
        if r < s or e < l:
            return
        if s <= l and r <= e:
            self.lazy[i] += v
            self.push(l, r, i)
            return
        mid = (l+r)//2
        self.update(l, mid, i*2, s, e, v)
        self.update(mid+1, r, i*2+1, s, e, v)
        self.tree[i] = self.tree[i*2]+self.tree[i*2+1]
        return

    def push(self, l, r, i):
        if self.lazy[i] != 0:
            self.tree[i] = (r-l+1 - self.tree[i])
            if l != r:
                self.lazy[i*2] ^= 1
                self.lazy[i*2+1] ^= 1
            self.lazy[i] = 0
        return

    def query(self, l, r, i, s, e):
        self.push(l, r, i)
        if r < s or e < l:
            return 0
        if s <= l and r <= e:
            return self.tree[i]
        mid = (l+r)//2
        lq = self.query(l, mid, i*2, s, e)
        rq = self.query(mid+1, r, i*2+1, s, e)
        totq = lq+rq
        return totq


N, M = map(int, input().split())
works = [list(map(int, input().split())) for _ in range(M)]


segtree = segTree([0 for _ in range(N)])
segtree.build(0, segtree.leng-1, 1)


ans_arr = []
for oper, s, e in works:
    if oper == 0:
        segtree.update(0, segtree.leng-1, 1, s-1, e-1, 1)
    else:
        ans = segtree.query(0, segtree.leng-1, 1, s-1, e-1)
        ans_arr.append(ans)


sys_print('\n'.join(map(str, ans_arr)))
