import sys
input = sys.stdin.readline
print = sys.stdout.write


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        # a>b에서는 RecursionError가 나고
        # a<b는 정상 통과된다.
        # union(9, 10)
        # union(8, 9)
        # ~~~
        # 와 같은 저격 데이터가 편향되어있다고 추측된다.
        parent[a] = b
    else:
        parent[b] = a


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES'+'\n')
        else:
            print('NO'+'\n')
