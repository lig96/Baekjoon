N = int(input())
M = int(input())
buttons = set(input().split()) if M > 0 else set()


ans = abs(N - 100)


for numbers in range(1_000_000+2):
    for number in str(numbers):
        if number in buttons:
            break
    else:
        ans = min(ans, abs(N-numbers)+len(str(numbers)))
print(ans)