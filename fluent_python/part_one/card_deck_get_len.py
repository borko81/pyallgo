import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __repr__(self):
        return f'Card is {self.ranks!r}'


if __name__ == '__main__':
    f = FrenchDeck()
    # print(len(f))
    first_five = [random.choice(f) for _ in range(5)]
    # print(first_five)
    # f._cards = [c for c in f._cards if c not in first_five]
    # print(len(f))
    [print(f"Rank is {i.rank} suit is {i.suit}") for i in first_five]
    print(f)
