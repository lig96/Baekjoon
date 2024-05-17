import sys
input = sys.stdin.readline


class segTree():
    def __init__(self, N):
        self._N = N
        return

    def build(self, arr):
        self.segtree = [None for _ in range(2*self._N)]
        for i in range(self._N):
            self.segtree[i+self._N] = arr[i]
        for i in range(self._N-1, 0, -1):
            self.segtree[i] = self.segtree[i << 1] + self.segtree[i << 1 | 1]
        return

    def execute(self, queries):
        for query in queries:
            a, b, c = query
            # 제로 인덱싱. 구간은 [start, end).
            if a == 1:
                self.update(b-1, c)
            elif a == 2:
                self.get_max(b-1, c)
            else:
                raise Exception
        return

    def update(self, ind, target):
        ind += self._N
        self.segtree[ind] = target
        while ind >= 2:
            self.segtree[ind >> 1] = self.segtree[ind] + self.segtree[ind ^ 1]
            ind >>= 1
        return

    def get_max(self, start, end):
        result = 0
        start += self._N
        end += self._N
        while start < end:
            if start & 1 == 1:  # 홀수라면
                result += self.segtree[start]
                start += 1
            if end & 1 == 1:  # 홀수라면
                result += self.segtree[end-1]
                end -= 1
            start >>= 1
            end >>= 1
        print(result)
        return


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(M+K)]


segtree = segTree(N)
segtree.build(arr)


segtree.execute(queries)
