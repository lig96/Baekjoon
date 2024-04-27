# 방법 1: full-batch, Adam Optimizer를 사용한 경사하강법
#
# 방법 2: 삼분탐색
# 될 것 같은데 절반 가량의 TC에서 300 정도 틀림.


import sys
input = sys.stdin.readline


def dist(a, b):
    '''
    If a is dot and b is dot, return squared Euclidean distance.
    If a is dot and b is arr of dots, return Euclidean distance.
    '''
    if type(b[0]) == int:
        return (a[0]-b[0])**2 + (a[1]-b[1])**2
    else:
        # 1500 ms
        # return sum(dist(a, dot_b)**(1/2) for dot_b in b)
        # 1200ms
        return sum(((a[0]-dot_b[0])**2 + (a[1]-dot_b[1])**2)**(1/2) for dot_b in b)


def grad(a, b_arr, dim):
    eps = 0.0001
    old_fx = dist(a, b_arr)
    a[dim] += eps
    new_fx = dist(a, b_arr)
    a[dim] -= eps
    return (new_fx-old_fx)/eps


def update_weights(ws, gs, ms, vs):
    '''
    adam optimizer
    '''
    for dim in range(2):
        ms[dim] = b1*ms[dim] + (1-b1)*gs[dim]
        vs[dim] = b2*vs[dim] + (1-b2)*(gs[dim]**2)
        t = epoch+1  # t는 1부터 시작
        unbiased_m = ms[dim]/(1-b1**t)
        unbiased_v = vs[dim]/(1-b2**t)
        ws[dim] -= (lr) * (unbiased_m) / ((unbiased_v**0.5)+1e-7)
    return ws


N = int(input())
computers = tuple(tuple(map(int, input().split())) for _ in range(N))


weights = [sum(x for x, _ in computers)//N,
           sum(y for _, y in computers)//N]  # 시작값은 임의값도 괜찮으나 휴리스틱으로 평균
momentums = [0 for _ in range(2)]
velocities = [0 for _ in range(2)]
lr, b1, b2 = 0.1, 0.9, 0.999
epochs = int(3e5) // N


if N <= 2:
    print(round(dist(computers[0], computers[-1])**0.5))
else:
    # while dist(dot_old, dot_new) > threshold:
    #     가능은 하지만 threshold 설정이 까다롭고 실수 오차 여지가 있음.
    #     pass
    for epoch in range(epochs):
        gs = [grad(weights, computers, dim) for dim in range(2)]
        weights = update_weights(weights, gs, momentums, velocities)

    print(round(dist(weights, computers)))
