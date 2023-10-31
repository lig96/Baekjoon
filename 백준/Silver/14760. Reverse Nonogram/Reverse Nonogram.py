import re
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(mat):
    for r_or_c in mat:
        Xss = re.findall('X+', ''.join(r_or_c))
        if Xss:
            temp = ' '.join(str(len(Xs)) for Xs in Xss)
        else:
            temp = '0'
        print(temp+'\n')


while n := int(input()):
    mat = [list(input().rstrip()) for _ in range(n)]
    sol(mat)
    mat = [x for x in zip(*mat)]  # 주의. 오른쪽으로 90도랑 다름.
    sol(mat)
