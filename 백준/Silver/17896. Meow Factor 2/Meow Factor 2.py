# https://leeingyun96.tistory.com/27

import re


S = input()


if 'make patterns using method 1':
    p0 = ['(meow)']
    p1 = ['(eow|mow|mew|meo)',  # insert
          '(me.ow)',  # delete
          '(m.ow|me.w)',  # replace
          '(moew)']  # swap
    # p1_untrimmed = [
    #     '(eow|mow|mew|meo)',  # insert
    #     '(m.eow|me.ow|meo.w)',  # delete
    #     '(.eow|m.ow|me.w|meo.)',  # replace
    #     '(m.eow|emow|moew|mowe|meo.w)'  # swap
    # ]
    p2 = ['(me|mo|mw|eo|ew|ow)|(m.o|e.w|m..w)|(em.w|m.wo)']
    # https://blog.naver.com/jinhan814/222509018511
    p3 = ['(m|e|o|w)']
else:
    def make_p(before):
        new = set()
        for v in before:
            for i in range(len(v)):
                new.add(v[:i]+v[i+1:])  # insert
                new.add(v[:i]+'.'+v[i+1:])  # replace
                if i >= 1:  # range(1, len(v))와 동일
                    new.add(v[:i]+'.'+v[i:])  # delete
                    new.add(v[:i-1] + v[i] + v[i-1] + v[i+1:])  # swap
        return new

    p0 = set(['meow'])
    p1 = make_p(p0)
    p2 = make_p(p1)
    p3 = set(['m', 'e', 'o', 'w'])
    # p3 = make_p(p2)
    # 근본적으로 동일하지만 substring 여부를 확인하지 않아서 비효율적.
    # 'm'만 있으면 되는데 'mew..' 등도 포함되어버림.


for i, p in enumerate([p0, p1, p2, p3]):
    if re.search('|'.join(p), S):
        print(i)
        break
else:
    print(4)
