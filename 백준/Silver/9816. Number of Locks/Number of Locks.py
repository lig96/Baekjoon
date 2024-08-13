from itertools import product
import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def ok(arr):
    cond1 = any(
        abs(arr[i]-arr[i+1]) == 3 for i in range(len(arr)-1)
    )
    cond2 = any(x == 0 for x in arr)
    return cond1 and cond2


def make_ans_arr(MODE):
    '''
    if MODE == 'make_precomputation',
    print the ans_arr and exit the program.
    '''
    if MODE == 'dp':
        ans_arr = [None for _ in range(17)]
        # 맨 오른쪽이 1인지
        # 맨 오른쪽이 4인지
        # 전체 중 2 혹은 3이 있는지
        # 전체 중 14 혹은 41이 있는지
        dp = [[0 for _ in range(1 << 4)] for _ in range(17)]
        dp[1][1 << 3] += 1  # 1 추가. 1000
        dp[1][1 << 1] += 1  # 2 추가. 0010
        dp[1][1 << 1] += 1  # 3 추가. 0010
        dp[1][1 << 2] += 1  # 4 추가. 0100
        for n in range(2, 17):
            for bit in range(1 << 4):
                # 1 추가
                new = bit
                new |= (1 << 3)
                new &= ~(1 << 2)
                new |= (0)
                new |= (((bit & 1 << 2) >> 2) << 0)
                dp[n][new] += dp[n-1][bit]
                # 2, 3 추가
                for _ in range(2):
                    new = bit
                    new &= ~(1 << 3)
                    new &= ~(1 << 2)
                    new |= (1 << 1)
                    new |= (0)
                    dp[n][new] += dp[n-1][bit]
                # 4 추가
                new = bit
                new &= ~(1 << 3)
                new |= (1 << 2)
                new |= (0)
                new |= (((bit & 1 << 3) >> 3) << 0)
                dp[n][new] += dp[n-1][bit]
            ans_arr[n] = sum(dp[n][bit] for bit in range(1 << 4)
                             if ((bit & 1 << 1) >> 1) & ((bit & 1 << 0) >> 0)
                             )
        return ans_arr
    elif MODE == 'make_precomputation':
        ans_arr = [None for _ in range(17)]
        for n in range(2, 17-6):
            # range(2,15)에 10분
            # 15에 30분?
            # 16에 90분?
            ans_arr[n] = sum(
                1 for perm in product([1, 0, 0, 4], repeat=n) if ok(perm)
            )
        print(f'ans_arr = {ans_arr}')
        exit()
    elif MODE == 'use_precomputation':
        ans_arr = [None,  # 0
                   None, 0, 8, 64, 360,  # 1..5
                   1776, 8216, 36640, 159624, 684240,  # 6..10
                   2898296, 12164608, 50687208, 209961648, 865509848,  # 11..15
                   3553389280  # 16
                   ]
        # 15, 16은 dp로 계산한 숫자
        return ans_arr

    raise Exception('wrong conditional branching')


MODE = ['dp',
        'make_precomputation',
        'use_precomputation'
        ][2]


input_datas = []
while (input_data := int(input())) != -1:
    input_datas.append(input_data)


ans_arr = make_ans_arr(MODE)


answers = [f'{x}: {ans_arr[x]}' for x in input_datas]


sys_print('\n'.join(answers))
