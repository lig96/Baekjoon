from collections import Counter
import sys
input = sys.stdin.readline


N = int(input())
numbers = [int(input()) for _ in range(N)]


numbers.sort()
tot_sum = sum(numbers)
mode_dict = Counter(numbers)

mean = round(tot_sum / N)
median = numbers[N//2]
sorted_mode_dict_keys = sorted(mode_dict.keys(),
                               key=lambda x: (-mode_dict[x], x))
if N > 1 and mode_dict[sorted_mode_dict_keys[0]] == mode_dict[sorted_mode_dict_keys[1]]:
    mode = sorted_mode_dict_keys[1]
else:
    mode = sorted_mode_dict_keys[0]
range_ = numbers[N-1] - numbers[0]


print(mean)
print(median)
print(mode)
print(range_)
