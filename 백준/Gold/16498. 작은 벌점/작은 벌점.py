from bisect import bisect_left
import sys
input = sys.stdin.readline


def two_nearest_cards(cards, x):
    ind = bisect_left(cards, x)
    if ind == 0:
        return (cards[ind],)
    elif ind == len(cards):
        return (cards[ind-1],)
    else:
        return (cards[ind-1], cards[ind])


A, B, C = map(int, input().split())
cards_list = [list(map(int, input().split())) for _ in range(3)]


for v in cards_list:
    v.sort()


min_penalty = float('inf')
for a in cards_list[0]:
    for b in two_nearest_cards(cards_list[1], a):
        for c in (two_nearest_cards(cards_list[2], b) +
                  two_nearest_cards(cards_list[2], a)):
            # b와 비슷한 두 카드 + a와 비슷한 두 카드
            min_penalty = min(
                min_penalty,
                (max(a, b, c) - min(a, b, c))
            )


print(min_penalty)
