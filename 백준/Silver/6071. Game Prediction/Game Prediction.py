import sys
input = sys.stdin.readline


def sol(m, n, cards):
    opp_cards = sorted(set(range(1, m*n+1)) - set(cards))
    cards.sort()

    win_cnt = n

    for card in reversed(cards):
        # not_played_opp = m-1

        if opp_cards[-1] > card:
            opp_cards.pop()
            # not_played_opp -= 1
            win_cnt -= 1

        # # opp_cards:deque를 오른쪽에서 접근하는 것과
        # # 왼쪽에서 접근하는 것이 서로 교차할 일이 없으므로
        # # 왼쪽에서 굳이 접근을 하지 않아도 된다.
        # for _ in range(not_played_opp):
            # opp_cards.popleft()
            # not_played_opp -= 1
    # assert not_played_opp == 0 and not opp_cards

    return win_cnt


for case in range(1, 9_999_999):
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break
    cards = []
    while len(cards) != n:
        cards.extend(map(int, input().split()))
    _ = input()

    ans = sol(m, n, cards)

    print(f"Case {case}: {ans}")
