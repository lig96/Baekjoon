_ = input()
numbers = input().split()

temp = sorted(numbers, key=lambda x: (x*10)[:10], reverse=True)
print(int(''.join(temp)))