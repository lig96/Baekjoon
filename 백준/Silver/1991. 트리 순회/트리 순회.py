N = int(input())
dic = {a: [b, c] for a, b, c in (input().split() for _ in range(N))}


def sol(node, op):
    if node == '.':
        return

    print(node, end='') if op == 'pre' else None
    sol(dic[node][0], op)
    print(node, end='') if op == 'in' else None
    sol(dic[node][1], op)
    print(node, end='') if op == 'post' else None


[(sol('A', op), print()) for op in ['pre', 'in', 'post']]
