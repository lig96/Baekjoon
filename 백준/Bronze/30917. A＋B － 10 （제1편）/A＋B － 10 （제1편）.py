# 인터랙티브


for a in range(1, 10):
    print(f'? A {a}', flush=True)
    if (resp := int(input())) == 1:
        break
for b in range(1, 10):
    print(f'? B {b}', flush=True)
    if (resp := int(input())) == 1:
        break


print(f'! {a+b}')
