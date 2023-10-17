import sys
print = sys.stdout.write


def rec(width):
    if width == 3:
        return ['***',
                '* *',
                '***']
    rows = rec(width//3)
    stars = []

    for row in rows:
        temp = row*3
        stars.append(temp)
    for row in rows:
        temp = row + ' '*(width//3) + row
        stars.append(temp)
    for row in rows:
        temp = row*3
        stars.append(temp)

    return stars


N = int(input())


ans = rec(N)


print('\n'.join(ans))