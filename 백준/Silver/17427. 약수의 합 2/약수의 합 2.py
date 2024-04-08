import sys
input = sys.stdin.readline
print = sys.stdout.write


def g(num):
    g_num = 0
    for i in range(1, num+1):
        cnt = num//i  # [1, num] 중 i의 배수의 개수
        tot = cnt * i  # 총합 = 개수 * 값
        g_num += tot
    return g_num


N = int(input())


print(str(g(N)))
