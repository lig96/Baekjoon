import sys
from collections import defaultdict
input = sys.stdin.readline
sys_print = sys.stdout.write


def factorization(dic, num):
    for i in [2, 5]:
        ij = i
        while ij <= num:
            dic[i] += num//ij
            ij *= i
    return


n, m = map(int, input().split())


n_dict = defaultdict(lambda: 0)  # factorization of n!
nm_dict = defaultdict(lambda: 0)  # factorization of (n-m)!
m_dict = defaultdict(lambda: 0)  # factorization of m!
factorization(n_dict, n)
factorization(nm_dict, n-m)
factorization(m_dict, m)


ans_dict = dict()
for i in [2, 5]:
    ans_dict[i] = n_dict[i] - (nm_dict[i] + m_dict[i])
ans = min(ans_dict.values())
sys_print(str(ans))


'''
nCm = 
    n!
---------
(n-m)! m!
'''
