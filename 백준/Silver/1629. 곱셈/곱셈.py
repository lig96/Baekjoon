A, B, C = map(int, input().split())


def dac(A, B, C):
    if B <= 2:
        temp = A ** B
    elif B % 2 == 1:
        temp = (dac(A, B//2, C) ** 2) * A
    elif B % 2 == 0:
        temp = (dac(A, B//2, C) ** 2)

    return temp % C


temp = dac(A, B, C)
print(temp % C)
