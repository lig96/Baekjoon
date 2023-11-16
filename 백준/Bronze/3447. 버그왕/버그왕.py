import re
import sys
print = sys.stdout.write


lines = sys.stdin.readlines()


for line in lines:
    line = line.rstrip()
    while True:
        line_after = re.sub('BUG', '', line)
        if line_after != line:
            line = line_after
        else:
            ans = line_after
            break

    print(ans+'\n')
