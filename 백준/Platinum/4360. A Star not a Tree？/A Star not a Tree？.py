# 방법 1: 경사하강법
# O(N * (EPOCHS*DIM))
#
# 방법 2: n차원 삼분탐색
# O(N * ((ITER*2)^DIM))


import sys
input = sys.stdin.readline


def dist(a, b):
    '''
    If a is dot and b is dot,
    return Euclidean dist between a and b.
    If a is dot and b is arr of dots,
    return summation of Euclidean dist between a and dot in b.
    '''
    if type(b[0]) == int:
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    else:
        # 1500 ms
        # return sum(dist(a, dot_b)**(1/2) for dot_b in b)
        # 1200ms
        return sum(((a[0]-dot_b[0])**2 + (a[1]-dot_b[1])**2)**0.5 for dot_b in b)


def ternary_search(lo, hi, point, dim):
    if dim == DIM:
        return (dist(point, computers), point)

    for _ in range(ITER):
        llh = lo + (hi-lo)*RATIO
        lhh = lo + (hi-lo)*(1-RATIO)

        point[dim] = llh
        value_llh, point_llh = ternary_search(LO, HI, point, dim+1)
        point[dim] = lhh
        value_lhh, point_lhh = ternary_search(LO, HI, point, dim+1)

        if value_llh < value_lhh:
            hi = lhh
        else:
            lo = llh
    return value_llh, point_llh


def grad(a, b_arr, dim):
    old_fx = dist(a, b_arr)

    a[dim] += EPS
    new_fx = dist(a, b_arr)
    a[dim] -= EPS
    return (new_fx-old_fx)/EPS


def update_weights(ws, gs, ms, vs):
    '''
    adam optimizer
    '''
    for dim in range(DIM):
        ms[dim] = b1*ms[dim] + (1-b1)*gs[dim]
        vs[dim] = b2*vs[dim] + (1-b2)*(gs[dim]**2)
        t = epoch+1  # t는 1부터 시작
        unbiased_m = ms[dim]/(1-b1**t)
        unbiased_v = vs[dim]/(1-b2**t)
        ws[dim] -= (lr) * (unbiased_m) / ((unbiased_v**0.5)+1e-7)
    return ws


N = int(input())
computers = tuple(tuple(map(int, input().split())) for _ in range(N))


MODE = ['gradient descent', 'ternary search'][
    0]
if MODE == 'gradient descent':
    DIM = 2
    weights = [sum(x for x, _ in computers)//N,
               sum(y for _, y in computers)//N]
    # 시작값은 임의값도 괜찮으나 휴리스틱으로 평균으로 잡음.
    momentums = [0 for _ in range(2)]
    velocities = [0 for _ in range(2)]
    lr, b1, b2 = 0.1, 0.9, 0.999
    EPOCHS = int(5e5) // N // DIM
    EPS = 1/2**10

    if N <= 2:
        print(round(dist(computers[0], computers[-1])))
    else:
        # while dist(dot_old, dot_new) > threshold:
        #     가능은 하지만 threshold 설정이 까다롭고 실수 오차 여지가 있음.
        #     pass
        for epoch in range(EPOCHS):
            gs = [grad(weights, computers, dim) for dim in range(DIM)]
            weights = update_weights(weights, gs, momentums, velocities)
        print(round(dist(weights, computers)))
elif MODE == 'ternary search':
    DIM = 2
    LO = 0
    HI = 10_000+1
    RATIO = 1/2 - 1/2**5   # 0.46875
    ITER = min(500, int((int(1e7)//N)**(1/DIM))//2)

    if N <= 2:
        print(round(dist(computers[0], computers[-1])))
    else:
        min_value, min_point = ternary_search(
            LO, HI, [None for _ in range(2)], 0
        )
        print(round(min_value))
