"""CSC 161 Lab: Classes

Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019
"""

from random import randrange


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


def make_random_cards(n):
    cards_list = []
    for i in range(n):
        rank = randrange(1, 14, 1)
        suitNum = randrange(1, 5, 1)
        if (suitNum == 1):
            suit = "d"
        elif (suitNum == 2):
            suit = "c"
        elif (suitNum == 3):
            suit = "h"
        elif (suitNum == 4):
            suit = "s"
        cards_list.append(PlayingCard(rank, suit))

    return cards_list


def main():
    n = eval(input('How many cards would you like to generate? '))
    cards = make_random_cards(n)
    for card in cards:
        print(card)


if __name__ == '__main__':
    main()
