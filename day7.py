import itertools
import more_itertools

from functools import cached_property
from collections import Counter


cards = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")

rankings = {card: r for r, card in enumerate(cards)}

rr = {card: r for r, card in enumerate(reversed(cards))}


class Hand:
    def __init__(self, hand: str) -> None:
        self.hand = ''.join(sorted([x for x in hand], key=rankings.get))
    
    @cached_property
    def counter(self):
        return Counter(self.hand)
    
    @cached_property
    def counts(self):
        return self.counter.values()
    
    def type_(self):
        return tuple(sorted(self.counts, reverse=True))
    
    def card_ranks(self):
        cs = []
        for card, cnt, in hand.counter.most_common():
            cs.append(card)

        css = [rr.get(c) for c in cs]

        return tuple(css)

    def rank(self):
        return (self.type_(), self.card_ranks())







# deck = []

# for card in cards:
#     deck.append(list(itertools.repeat(card, 5)))

# deck = list(more_itertools.flatten(deck))

# all_hands = list(more_itertools.distinct_combinations(deck, 5))




hand = "32T3K"




test_hands = ["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"]




# with open("input7.txt") as f:
#     for line in f:
#         hand, bet = line.split()
#         s = sort_hand(hand)
#         print(f"{hand} --> {s}")
#         print(rank(s))



ranks = []

for h in test_hands:
    hand = Hand(h)
    print(f"{h} --> {hand.hand}")
    print(hand.rank())
    ranks.append(hand.rank())