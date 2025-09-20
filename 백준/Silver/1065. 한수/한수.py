import sys
input = sys.stdin.readline


def sol(N) -> int:
    def hansu(x: int) -> bool:
        x = str(x)

        if len(x) == 1:
            return True

        d = int(x[1]) - int(x[0])
        for i in range(len(x)-1):
            if (int(x[i]) + d) != int(x[i+1]):
                return False
        return True

    ret = sum(hansu(i) for i in range(1, N+1))
    return ret


N = int(input())


print(sol(N))
