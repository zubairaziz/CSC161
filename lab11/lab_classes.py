class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.bj_value()

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def bj_value(self):
        if (self.rank > 10):
            self.value = 10
        else:
            self.value = self.rank
        return self.value

    def __repr__(self):
        ranks = [None, "Ace", 2, 3, 4, 5, 6, 7,
                 8, 9, 10, "Jack", "Queen", "King"]
        suits = {"d": "Diamonds", "c": "Clubs", "h": "Hearts", "s": "Spades"}
        rank = ranks[self.rank]
        suit = suits[self.suit]
        value = self.value
        return "{0} of {1} counts {2}".format(rank, suit, value)


def main():
    c = PlayingCard(1, "s")
    print(c)
    c2 = PlayingCard(12, "c")
    print(c2)
    print(c2.bj_value())
    print(c2.get_rank())
    print(c2.get_suit())


if __name__ == '__main__':
    main()
