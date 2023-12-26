# 방법 1.
# round는 4자리라고 써도 50.0까지만 출력한다.
# 별도의 후처리를 통해 '0'을 추가한다.

# 방법 2.
# 파이썬 문자열 포맷팅은 반올림의 기능도 있으며
# .4f라고 하면 정확히 4자리를 출력한다.
# print(f'{k} {v/cnt*100:.4f}')


from collections import defaultdict
import sys
print = sys.stdout.write


lines = sys.stdin.readlines()


dic = defaultdict(lambda: 0)
cnt = len(lines)


for line in lines:
    line = line.rstrip()
    dic[line] += 1


for k, v in sorted(dic.items()):
    v = str(round((v*100/cnt), 4))
    v = v + '0' * (4-((len(v)-1)-v.find('.')))
    print(k+' '+str(v)+'\n')
