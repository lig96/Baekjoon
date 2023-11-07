import re


if re.fullmatch('(100+1+|01)+', input()):
    print('SUBMARINE')
else:
    print('NOISE')
