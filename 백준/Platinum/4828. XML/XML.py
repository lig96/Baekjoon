import re
import sys


def sol(s):
    # 1. 32 ~ 127 검사. 해당 코드는 불필요하다.
    # char32 = chr(32)
    # char127 = chr(127)
    # temp = re.search(f'[^{char32}-{char127}]', s)
    # if temp:
    #     return 'invalid'

    # 1. <> 검사.
    if 'method 1':
        temp = re.findall('<', s)  # 올바른 <, 틀린 <
        temp2 = re.findall('>', s)  # 올바른 >, 틀린 >
        temp3 = re.findall(
            '(<[0-9a-z]+>)|(</[0-9a-z]+>)|(<[0-9a-z]+/>)',
            s)  # 올바른 <tag>
        if not (len(temp) == len(temp2) == len(temp3)):
            return 'invalid'
    elif 'method 2':
        temp = re.findall(
            '(<[0-9a-z]+>)|(</[0-9a-z]+>)|(<[0-9a-z]+/>)|([<>])',
            s)  # 틀린 <, >
        temp = [x[3] for x in temp if x[3]]
        if temp:
            return 'invalid'

    # 23. 문자열 검사
    # 대체가 아니라 제거해야 함. 반례 &lt;tag&gt;
    s = re.sub('&lt;|&gt;|&amp;', '', s)

    # 1. & 검사. 4. HEX 검사.
    if 'method 1':
        temp = re.findall(
            '&x([0-9A-Fa-f][0-9A-Fa-f])+;',
            s)  # & 뒤 올바른 HEX
        temp2 = re.findall('&', s)  # &
        if len(temp) != len(temp2):
            return 'invalid'
    elif 'method 2':
        temp = re.findall(
            '&(?!x([0-9A-Fa-f][0-9A-Fa-f])+;)',
            s)  # & 뒤 올바른 HEX가 오지 않는 경우
        if temp:
            return 'invalid'

    # 567. 스택 검사.
    stack = []
    temp = re.findall(
        '<([0-9a-z]+)>|<([0-9a-z]+)/>|</([0-9a-z]+)>',
        s)
    for a, b, c in temp:
        # 여는 태그, pass 태그, 닫는 태그
        if a:
            stack.append(a)
        elif b:
            pass
        elif c:
            if not stack:
                return 'invalid'
            popped = stack.pop()
            if popped != c:
                return 'invalid'
    if stack:
        return 'invalid'
    else:
        return 'valid'


for s in sys.stdin.readlines():
    s = s.rstrip()

    print(sol(s))
