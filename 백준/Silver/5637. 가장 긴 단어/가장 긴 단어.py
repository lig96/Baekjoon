import re
import sys


ans = ''


for line in sys.stdin.readlines():
    line = line.rstrip()
    temp_arr = re.findall('[a-zA-Z-]{1,}', line)

    for temp in temp_arr:
        if len(temp) > len(ans):
            ans = temp


print(ans.lower())
