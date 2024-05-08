import sys
input = sys.stdin.readline


for _ in range(T := int(input())):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = [None for _ in range(N)]
    # max_price[i] = max(prices[i:])
    temp = -float('inf')
    for i in range(N)[::-1]:
        if prices[i] > temp:
            temp = prices[i]
            max_price[i] = temp
        else:
            max_price[i] = temp

    ans = 0
    for i, price in enumerate(prices):
        if price < max_price[i]:
            ans += max_price[i] - price

    print(ans)
