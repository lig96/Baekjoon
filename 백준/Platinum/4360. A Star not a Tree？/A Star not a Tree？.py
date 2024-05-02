# 방법 1: 경사하강법
# O(N * (EPOCHS*DIM))
#
# 방법 2: n차원 삼분탐색
# O(N * ((ITER*2)^DIM))
# 여기서 2는 llh, lhh.


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


def grad(center, dots):
    '''
    f(center) = dist(c,0) + dist(c,1) + ~~~
    f'(center) = dist'(c,0) + dist'(c,1) + ~~~
    dist(c, dot) = ((a-x)^2+(b-y)^2)^0.5
    dist'(c, dot) = (0.5*((a-x)^2+(b-y)^2)^-0.5)*(2*(a-x)*(-1))
    dist'(c, dot) = (x-a) / dist(c, dot)
    center = c = (x, y)이고 x에 대해 편미분하였을 때.

    대수적 방법말고 eps로 구하는 것도 정답 판정 받음.
    '''
    temp = [0 for _ in range(DIM)]
    for dot in dots:
        d = dist(center, dot)
        for i in range(DIM):
            temp[i] += ((center[i]-dot[i]) / d) if d != 0 else 0
    return temp


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


def ternary_search(lo, hi, point, dim):
    if dim == DIM:
        return (dist(point, dots), point)

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
    # value는 원래 lo, llh, lhh, hi 중 최솟값 출력해야 하는데
    # 오차가 작아서 lhh로 출력함.
    # 얕은 복사 때문에 (point_llh is point_lhh)
    return value_lhh, point_lhh


N = int(input())
dots = tuple(tuple(map(int, input().split())) for _ in range(N))


MODE = ['gradient descent', 'ternary search'][
    0]
if MODE == 'gradient descent':
    DIM = 2
    weights = [sum(x for x, _ in dots)//N,
               sum(y for _, y in dots)//N]
    # 시작값은 임의값도 괜찮으나 휴리스틱으로 평균으로 잡음.
    momentums = [0 for _ in range(DIM)]
    velocities = [0 for _ in range(DIM)]
    lr, b1, b2 = 0.1, 0.9, 0.999
    EPOCHS = int(5e5 / N / DIM)

    if N <= 2:
        print(round(dist(dots[0], dots[-1])))
    else:
        # while dist(dot_old, dot_new) > threshold:
        #     가능은 하지만 threshold 설정이 까다롭고 실수 오차 여지가 있음.
        #     pass
        for epoch in range(EPOCHS):
            gs = grad(weights, dots)
            weights = update_weights(weights, gs, momentums, velocities)
        print(round(dist(weights, dots)))
elif MODE == 'ternary search':
    DIM = 2
    LO = 0
    HI = 10_000 + 1
    RATIO = 1/2 - 1/2**5   # 0.46875
    ITER = min(500, int((int(1e7)//N)**(1/DIM))//2)

    if N <= 2:
        print(round(dist(dots[0], dots[-1])))
    else:
        min_value, min_point = ternary_search(
            LO, HI, [None for _ in range(DIM)], 0
        )
        print(round(min_value))
