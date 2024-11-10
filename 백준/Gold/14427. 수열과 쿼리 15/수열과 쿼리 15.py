import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


class segTree():
    def __init__(self, arr):
        self.arr = arr
        self.leng = len(self.arr)
        self.tree = [None for _ in range(4*self.leng)]
        _ = self.build(0, self.leng-1, 1)
        return

    def build(self, l, r, i):
        if l == r:
            self.tree[i] = (l, self.arr[l])
            return self.tree[i]
        mid = (l+r)//2
        lv = self.build(l, mid, i*2)
        rv = self.build(mid+1, r, i*2+1)
        self.tree[i] = lv if lv[1] <= rv[1] else rv
        # 동순위일 때는 left 사용
        return self.tree[i]

    def update(self, l, r, i, ind, val):
        if ind < l or r < ind:
            return self.tree[i]
        if l == r == ind:
            self.tree[i] = (l, val)
            return self.tree[i]
        mid = (l+r)//2
        lv = self.update(l, mid, i*2, ind, val)
        rv = self.update(mid+1, r, i*2+1, ind, val)
        self.tree[i] = lv if lv[1] <= rv[1] else rv
        return self.tree[i]

    def query(self, l, r, i, s, e):
        if r < s or e < l:
            return (float('inf'), float('inf'))
        if s <= l and r <= e:
            return self.tree[i]
        mid = (l+r)//2
        lv = self.query(l, mid, i*2, s, e)
        rv = self.query(mid+1, r, i*2+1, s, e)
        ret = lv if lv[1] <= rv[1] else rv
        return ret


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
queries = [list(map(int, input().split())) for _ in range(M)]


segtree = segTree(arr)


ans_arr = []
for query in queries:
    if query[0] == 1:
        _, ind, val = query
        segtree.update(0, N-1, 1, ind-1, val)
    elif query[0] == 2:
        ans = segtree.query(0, N-1, 1, 0, N-1)[0] + 1
        ans_arr.append(ans)
    else:
        raise Exception


sys_print('\n'.join(map(str, ans_arr)))
