# 하나씩 print
# 하나씩 sys_print
# 모아서 sys_print
# 다 엇비슷함


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
        if l == r:
            self.tree[i] = self.arr[l]
            return
        mid = (l+r)//2
        self.build(l, mid, i*2)
        self.build(mid+1, r, i*2+1)
        self.tree[i] = sum((self.tree[i*2], self.tree[i*2+1]))
        return

    def update(self, l, r, i, s, e, diff):
        self.push(l, r, i)
        if r < s or e < l:
            return
        if s <= l and r <= e:
            self.lazy[i] += diff
            self.push(l, r, i)
            return
        mid = (l+r)//2
        self.update(l, mid, i*2, s, e, diff)
        self.update(mid+1, r, i*2+1, s, e, diff)
        self.tree[i] = self.tree[i*2]+self.tree[i*2+1]
        return

    def push(self, l, r, i):
        if self.lazy[i] != 0:
            # print(self.tree[i], 'before')
            self.tree[i] += (r-l+1) * self.lazy[i]
            # print(self.tree[i], 'after')
            # print(self.tree)
            if l != r:
                self.lazy[i*2] += self.lazy[i]
                self.lazy[i*2+1] += self.lazy[i]
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
        ret = lq + rq
        return ret


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [list(map(int, input().split())) for _ in range(M+K)]


segtree = segTree(arr)
segtree.build(0, segtree.leng-1, 1)


ans_arr = []
for oper, *query in queries:
    if oper == 1:
        b, c, d = query
        segtree.update(0, segtree.leng-1, 1, b-1, c-1, d)
    else:
        b, c = query
        ans = segtree.query(0, segtree.leng-1, 1, b-1, c-1)
        ans_arr.append(ans)


sys_print('\n'.join(map(str, ans_arr)))
