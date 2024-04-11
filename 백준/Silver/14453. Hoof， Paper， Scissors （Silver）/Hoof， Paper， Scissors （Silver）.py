import sys
input = sys.stdin.readline


def a_wins_against_b(a, b):
    temp = (a, b)
    if temp == ('H', 'S'):
        return True
    elif temp == ('S', 'P'):
        return True
    elif temp == ('P', 'H'):
        return True
    else:
        return False


def what_loses_against(v):
    if v == 'H':
        return 'S'
    elif v == 'S':
        return 'P'
    else:
        return 'H'


N = int(input())
john_gestures = [input().rstrip() for _ in range(N)]


right_sum_arr = {v: john_gestures.count(what_loses_against(v))
                 for v in 'HPS'}
ans = -float('inf')


for left, right in [('H', 'P'), ('H', 'S'),
                    ('P', 'H'), ('P', 'S'),
                    ('S', 'H'), ('S', 'P')]:
    left_sum = 0
    right_sum = right_sum_arr[right]
    ans = max(ans, left_sum+right_sum)

    for v in john_gestures:
        if a_wins_against_b(left, v):
            left_sum += 1
        elif a_wins_against_b(right, v):
            right_sum -= 1
        ans = max(ans, left_sum+right_sum)


print(ans)
