import re
import sys


p = re.compile('da+dd?(i|y)')


for line in sys.stdin.readlines():
    line = line.rstrip()
    if p.fullmatch(line):
        print('She called me!!!')
    else:
        print('Cooing')
