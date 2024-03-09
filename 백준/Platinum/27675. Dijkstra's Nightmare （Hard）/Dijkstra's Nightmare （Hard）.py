# 아이디어: 지수함수 꼴이 되도록 재귀를 시켜준다.
# 구현: 비트와이즈 연산자를 사용한다.
# 주의: 초항이 1이 아니라 2 혹은 3이다.
# 주의: 음수를 *2씩 해줘야지, 16 > 8+4+2+1라서
#       여전히 음수가 된다.
# 주의: 이때 2^start정점이 아니라
#      윗 방향으로 (8+4+2+1), 4개라는 true_s를 따로 센다.

'''
51 ~ 58
\ | /
2 ~ 50
\ | /
  1
  | \ 
  0-59
0번 - 442 -> 443번

0-59를 bignum으로 뻗은 뒤 59-1를 뻗는 선을 음수로 한다면?
0번 - 442 - 59번 - 442 =
0번 - 442*2 - 59번 -> 886번
도합 (x-1)*2+1+1 -> 2x번

1->그래프

59->1

x->59->1
x->1

y->x->59->1
y->x->1
y->59->1
y->1

y에서 x로 뻗고, 59로 뻗고, ~~~,  1로 뻗음.
이런 형태여야 2^V 꼴이 가능함.


0-59를 bignum으로 뻗은 뒤 59-1를 뻗는 선도 bignum으로 한다면?
0번 - 442 - 59번  -> 444번
도합 x+1번

비트연산자로 2 혹은 3에서 x*2 혹은 (x*2)+1을 반복한다.

초항이 1이 아님에 유의.

2^s가 아니라 2^true_s임에 유의.
'''


from heapq import heappush, heappop
import sys


def refer_func():
    # read the number of vertices and the number of directed edges
    N = int(input())
    assert 1 <= N <= 60

    M = int(input())
    assert 0 <= M <= N*(N-1)

    # read the list of edges, check that there are no duplicates
    outgoing_edges = [{} for n in range(N)]

    for m in range(M):
        v_from, v_to, length = [int(x) for x in input().split()]

        assert 0 <= v_from <= N-1
        assert 0 <= v_to <= N-1
        assert -(2**31) <= length <= (2**31)-1

        assert v_from != v_to
        assert v_to not in outgoing_edges[v_from]

        outgoing_edges[v_from][v_to] = length

    # initialize the list of distances
    distance = [10**18 for n in range(N)]
    distance[0] = 0

    # initialize the priority queue
    priority_queue = []
    heappush(priority_queue, (0, 0))

    # main loop: while there is an active vertex, process it
    PROCESSED_VERTICES = 0

    while len(priority_queue) > 0:
        how_far, where = heappop(priority_queue)
        if distance[where] != how_far:
            continue  # discarding an old record

        PROCESSED_VERTICES += 1

        for goal in outgoing_edges[where]:
            t = how_far + outgoing_edges[where][goal]
            if t < distance[goal]:
                distance[goal] = t
                heappush(priority_queue, (t, goal))
            else:
                print(t-distance[goal], 'lack')
                print(where, goal)

    return PROCESSED_VERTICES


def is_negative_cycle():
    N = int(input())
    M = int(input())
    edges = []
    for m in range(M):
        try:
            edges.append(tuple(int(x) for x in input().split()))
        except Exception as E:
            print('Too Big M. M should be', m)
            print('E is', E)
            exit()
    try:
        _ = input()
    except EOFError:
        pass
    else:
        print('Too short M.')
        print('Input is', _)
        exit()

    distance = [10**18 for _ in range(N)]
    distance[0] = 0

    for _ in range(N-1):
        for s, e, c in edges:
            if distance[s] == 10**18:
                continue
            t = distance[s] + c
            if distance[e] > t:
                distance[e] = t
    else:
        for s, e, c in edges:
            if distance[s] == 10**18:
                continue
            t = distance[s] + c
            if distance[e] > t:
                distance[e] = t
                return True
    return False


def sol():
    '''
    PROCESSED_VERTICES가 target이 되는
    그래프를 출력 혹은 input.txt 파일로 저장함
    '''
    t = []

    if target == 1:
        s, e, c = 58, 59, 0
        t.append((s, e, c))
    else:
        if bin_target[:2] == '10':  # 2라면
            s, e, c = 0, 1, bignum
            t.append((s, e, c))
            nxt = 2
        elif bin_target[:2] == '11':  # 3이라면
            s, e, c = 0, 1, bignum
            t.append((s, e, c))
            s, e, c = 0, 2, bignum
            t.append((s, e, c))
            nxt = 3
        true_s = 0  # 2**0 = 1

        for i in range(2, len(bin_target)):
            if bin_target[i] == '0':
                s, e, c = 0, nxt, bignum
                t.append((s, e, c))
                for j in range(1, nxt):
                    s, e = nxt, j
                    c = -2**(true_s)
                    t.append((s, e, c))
                nxt += 1
                true_s += 1
            elif bin_target[i] == '1':
                s, e, c = 0, nxt, bignum
                t.append((s, e, c))
                for j in range(1, nxt):
                    s, e = nxt, j
                    c = -2**(true_s)
                    t.append((s, e, c))
                nxt += 1
                true_s += 1
                #
                s, e, c = 0, nxt, bignum
                t.append((s, e, c))
                nxt += 1
                # true_s += 그대로.
                # 지금 음수 c를 안 해줬기 때문에
                # 미래의 c가 작아도 중간의 음수들의 합보다 큼.

    if for_bj:
        file = sys.stdout
        file.write(str(60)+'\n')
        file.write(str(len(t))+'\n')
        for s, e, c in t:
            file.write(str(s)+' '+str(e)+' '+str(c)+'\n')
    else:
        file = open(path, 'w')
        file.write(str(60)+'\n')
        file.write(str(len(t))+'\n')
        for s, e, c in t:
            file.write(str(s)+' '+str(e)+' '+str(c)+'\n')
        file.close()
    return


# 입력
original_sys_stdin = sys.stdin
T = int(input())
for _ in range(T):
    _ = input()
    target = int(input())
    # print('Working on a target', target)

    # 준비 및 함수
    bignum = (2**31)-1
    bin_target = bin(target)[2:]
    # print(bin(10_000_000))
    # 0b_100_110_001_001_011_010_000_000
    # 24자리
    for_bj = True
    path = "input_for_bj_27675.txt"

    # 풀이
    sol()

    # 검산
    if for_bj:
        pass
    else:
        sys.stdin = open(path, "r")
        if is_negative_cycle():
            print('negative cycle')
            print('target is', target)
            sys.stdin.close()
            exit()
        sys.stdin.close()

        sys.stdin = open(path, "r")
        ans = refer_func()
        if ans != target:
            print('wrong PROCESSED_VERTICES')
            print('ans, target', ans, target)
            sys.stdin.close()
            exit()
        sys.stdin.close()

        sys.stdin = original_sys_stdin

    # print('Finished on a target', target)
