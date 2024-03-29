import sys
import re


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


numerator = 0
denominator = 0


words = set()
for line in sys.stdin.readlines():
    line = line.rstrip()
    for word in re.findall('[a-zA-Z]+', line):
        if word == 'BULLSHIT':
            numerator += len(words)
            denominator += 1
            words.clear()
        else:
            word = word.lower()
            words.add(word)


gcd = get_gcd(numerator, denominator)
numerator, denominator = numerator//gcd, denominator//gcd
print(f'{numerator} / {denominator}')
