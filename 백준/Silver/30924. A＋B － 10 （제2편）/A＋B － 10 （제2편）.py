# 인터랙티브


import random
import sys
input = sys.stdin.readline


used_set = set()
while True:
    while True:
        a = random.randrange(1, 10_000+1)
        if a not in used_set:
            used_set.add(a)
            break
    print(f'? A {a}', flush=True)
    if (resp := int(input())) == 1:
        break
used_set = set()
while True:
    while True:
        b = random.randrange(1, 10_000+1)
        if b not in used_set:
            used_set.add(b)
            break
    print(f'? B {b}', flush=True)
    if (resp := int(input())) == 1:
        break


print(f'! {a+b}')
