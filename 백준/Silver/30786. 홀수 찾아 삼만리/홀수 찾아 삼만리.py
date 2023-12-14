# s-m-e를 0-s, 0-m, 0-m, 0-e로 변환 시킴
# 중간 지점은 2번씩 카운팅되니 언제나 짝수고
# 첫 지점과 마지막 지점이 (홀짝),(짝홀)이라면 합은 짝수
# 딱 2개만 있으면 되니 flag로 구현


import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(spots):
    is_odd, is_even = False, False
    # 변경이 된다면 i+1, 즉 1 이상이니 언제나 True
    for i, (x, y) in enumerate(spots):
        temp = ((x+y) % 2 == 0)
        if temp:
            is_even = i+1
        else:
            is_odd = i+1
        if is_odd and is_even:
            break

    if is_odd and is_even:
        return (is_odd, is_even)
    else:
        return False


N = int(input())
spots = [list(map(int, input().split())) for _ in range(N)]


ans = sol(spots)


if ans:
    print('YES'+'\n')
    print(str(ans[0])+' ')
    for i in range(1, N+1):
        if i not in ans:
            print(str(i)+' ')
    print(str(ans[1])+' ')
else:
    print('NO')
