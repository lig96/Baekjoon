import re


def is_slump(s):
    if re.fullmatch('((D|E)F+)+G', s):
        return True
    else:
        return False


def is_slimp(s):
    if re.fullmatch('AH', s):
        return True
    elif re.fullmatch('AB.*C', s):
        return is_slimp(s[2:-1])
    elif re.fullmatch('A.*C', s):
        return is_slump(s[1:-1])
    else:
        return False


def is_slurpy(s):
    for middle in range(len(s)+1):
        left, right = s[:middle], s[middle:]
        if is_slimp(left) and is_slump(right):
            return True
    return False


print('SLURPYS OUTPUT')
for _ in range(int(input())):
    s = input()
    if is_slurpy(s):
        print('YES')
    else:
        print('NO')
print('END OF OUTPUT')
