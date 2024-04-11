import sys
input = sys.stdin.readline
print = sys.stdout.write


def eratostenes_sieve(f):
    for i in range(1, max_N+1):
        for j in range(1, (max_N//i)+1):
            f[i*j] += i
    return f


def make_prefix_sum(f, g):
    for i in range(1, max_N+1):
        g[i] = g[i-1] + f[i]
    return g


T = int(input())
N_arr = [int(input()) for _ in range(T)]


max_N = max(N_arr)
f = [0 for _ in range(max_N+1)]
g = [0 for _ in range(max_N+1)]


f = eratostenes_sieve(f)
g = make_prefix_sum(f, g)


print('\n'.join(map(lambda x: str(g[x]), N_arr)))
