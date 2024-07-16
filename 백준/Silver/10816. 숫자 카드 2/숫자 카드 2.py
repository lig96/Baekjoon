from collections import defaultdict
import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))


dic = defaultdict(lambda: 0)
for card in cards:
    dic[card] += 1
ans_arr = []
for number in numbers:
    ans_arr.append(dic[number])


sys_print(' '.join(map(str, ans_arr)))
