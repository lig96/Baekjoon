N = input()
numbers = input().split()


numbers.sort(key=lambda x: (x*10), reverse=True)


print(int(''.join(numbers)))
