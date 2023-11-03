import sys
import re

lines = sys.stdin.readlines()

begin = '\\begin{thebibliography}{99}\n'
ind = lines.index(begin)
text, bib = lines[:ind], lines[ind:]


p = re.compile(r'\\bibitem\{(.+?)\}')
bib_order = []
bib_dic = {}
for line in bib:
    cites = p.findall(line)
    for cite in cites:
        bib_dic[cite] = line
        bib_order.append(cite)
# dict[사람] = 사람. 사람. 년도.

p = re.compile(r'\\cite\{(.+?)\}')
correct_order = []
ans_from_text = []
ans_from_text.append(begin)
for line in text:
    cites = p.findall(line)
    for cite in cites:
        ans_from_text.append(bib_dic[cite])
        correct_order.append(cite)
end = '\\end{thebibliography}'  # readlines() 맨 뒤에는 \n이 없음
ans_from_text.append(end)


# if bib_order == correct_order:
# print('Correct')
#     print(begin, end='')
#     for x in correct_order:
#         print(bib_dic[x], end='')
#     print(end)

# if ''.join(bib) == ''.join(ans_from_text):
#     print('Correct')

# print(bib)
# print(list(ans_from_text[-1]))
# exit()
# if bib[-1][-1] == '\n':
#     raise Exception

if bib_order == correct_order:

# if bib == ans_from_text:
    print('Correct')
else:
    print('Incorrect')
    for i in ans_from_text:
        sys.stdout.write(i)
