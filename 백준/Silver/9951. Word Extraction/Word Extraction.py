import re
import sys

for line in sys.stdin.readlines():
    line = line.rstrip()
    if line == '#':
        continue
    line = line.lower()
    #
    line = re.sub(r'[^a-z0-9 ]*', '', line)
    #
    line = re.sub(r' [0-9]* ', ' ', line)  # 중간
    line = re.sub(r'^[0-9]* ', ' ', line)  # 시작
    line = re.sub(r' [0-9]*$', ' ', line)  # 끝
    #
    line = re.sub(r' {1,}', ' ', line)
    #

    ans = set(line.split())
    ans = sorted(list(ans))
    print('\n'.join(ans))
    print()
