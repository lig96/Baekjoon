import sys
print = sys.stdout.write


def rec(num, s, e, m):
    if num == 1:
        print(str(s)+' '+str(e)+'\n')
        return
    rec(num-1, s, m, e)
    print(str(s)+' '+str(e)+'\n')
    rec(num-1, m, e, s)
    return


N = int(input())


print(str(2**N-1)+'\n')
rec(N, 1, 3, 2)
