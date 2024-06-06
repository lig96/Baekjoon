import sys
input = sys.stdin.readline


N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))


tot_cost = 0
lowest_price = float('inf')
for now in range(N-1):
    needed_gas = roads[now]
    lowest_price = min(lowest_price, prices[now])
    tot_cost += needed_gas * lowest_price


print(tot_cost)
