# 'sys.stdin.readlines()에는 \n이 들어있고 맨 마지막 줄에는 \n이 없다'
# 라고 알고 있고 실제로도 그러한데
# 백준 채점 방식에서는 마지막 줄에도 \n이 붙는 듯하다.
# 문제 자체는 간단했으나 디버깅하기 어려웠다.

import sys
import re


is_text = True
p = re.compile(r'\{(.+?)\}')
now_order, correct_order = [], []
bib_dic = {}


for line in sys.stdin.readlines():
    line = line.rstrip()  # 라인 A
    if line == '\\begin{thebibliography}{99}':
        is_text = False

    if is_text:
        cites = p.findall(line)
        for cite in cites:
            correct_order.append(cite)
    else:
        cites = p.findall(line)
        for cite in cites:
            now_order.append(cite)
            bib_dic[cite] = line


# 입력된 bib에는 thebib, 99, ~~, thebib이 들어있음.
if now_order[2:-1] == correct_order:
    print('Correct')
else:
    print('Incorrect')
    print('\\begin{thebibliography}{99}')
    for i in correct_order:
        sys.stdout.write(bib_dic[i]+'\n')
    print('\\end{thebibliography}')
