import sys
import re

lines = sys.stdin.readlines()
begin = '\\begin{thebibliography}{99}\n'
ind = lines.index(begin)
text, bib = lines[:ind], lines[ind:]


p = re.compile(r'\\bibitem\{(.+?)\}')
bib_dic = {}
for line in bib:
    cites = p.findall(line)
    for cite in cites:
        bib_dic[cite] = line
# dict[사람] : 사람. 사람. 년도.

p = re.compile(r'\\cite\{(.+?)\}')
ans_from_text = []
ans_from_text.append(begin)
for line in text:
    cites = p.findall(line)
    for cite in cites:
        ans_from_text.append(bib_dic[cite])
end = '\\end{thebibliography}\n'  # readlines() 맨 뒤에는 \n이 없음
ans_from_text.append(end)


if bib == ans_from_text:
    print('Correct')
else:
    print('Incorrect')
    print(''.join(ans_from_text))
