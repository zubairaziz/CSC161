"""CSC 161 Lab: Data Collections

This lab generates the frequency distribution of each rank-suit combination
of a list of randomly generated cards
Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019
"""

from random import randrange
from lab_classes import PlayingCard
from math import sqrt
import lab_classes

suit_size = 13  # Number of cards in a suit.
deck_size = 52  # Number of cards in a deck.
num_cards = 260  # Number of cards to create with random rank & suit values


def make_random_cards():
    """Generate num_cards number of random PlayingCard objects.

    This function will generate num_cards RANDOM playing cards
    using your PlayingCard class. That means you will have to choose a random
    suit and rank for a card num_cards times.

    Printing:
        Nothing

    Positional arguments:
        None

    Returns:
        cards_list -- a list of PlayingCard objects.
    """
    cards_list = []
    for i in range(num_cards):
        rank = randrange(1, suit_size + 1, 1)
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


def freq_count(cards_list):
    """Count every suit-rank combination.

    Returns a dictionary whose keys are the card suit-rank and value is the
    count.

    Printing:
        Nothing

    Positional arguments:
        cards_list -- A list of PlayingCard objects.

    Returns:
        card_freqs -- A dictionary whose keys are the single letter in the set
        'd', 'c', 'h', 's' representing each card suit.  The value for each key
        is a list containing the number of cards at each rank, using the index
        position to represent the rank. For example, {'s': [0, 3, 4, 2, 5]}
        says that the key 's', for 'spades' has three rank 1's (aces), four
        rank 2's (twos), two rank 3's (threes) and 5 rank 4's (fours).  Index
        position 0 is 0 since no cards have a rank 0, so make note.
    """
    # DO NOT REMOVE BELOW
    if type(cards_list) != list or \
            list(filter(lambda x: type(x) != PlayingCard, cards_list)):
        raise TypeError("cards_list is required to be a list of PlayingCard \
                        objects.")
    # DO NOT REMOVE ABOVE

    card_freqs = {
        'd': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'c': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'h': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        's': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    for i in range(len(cards_list)):
        current_card = cards_list[i]
        suit = current_card.get_suit()
        rank = current_card.get_rank()
        card_freqs[suit][rank] += 1
    return card_freqs


def std_dev(counts):
    """Calculate the standard deviation of a list of numbers.

    Positional arguments:
        counts -- A list of ints representing frequency counts.

    Printing:
        Nothing

    Returns:
        _stdev -- The standard deviation as a single float value.
    """
    # DO NOT REMOVE BELOW
    if type(counts) != list or \
            list(filter(lambda x: type(x) != int, counts)):
        raise TypeError("counts is required to be a list of int values.")
    # DO NOT REMOVE ABOVE

    _stdev = 0.0
    weight_sum = 0
    diff_sq_sum = 0
    average_rank = 0
    count_sum = sum(counts)
    for i in range(len(counts)):
        weight_sum += (counts[i]*(i))
    average_rank = weight_sum/count_sum
    for i in range(len(counts)):
        diff_sq_sum += (counts[i]*((i+1) - average_rank)**2)
    _stdev += (sqrt(diff_sq_sum/count_sum))
    return _stdev


def print_stats(card_freqs):
    """Print the final stats of the PlayingCard objects.

    Positional arguments:
        card_freqs -- A dictionary whose keys are the single letter in the set
        'dchs' representing each card suit. The value for each key is a list of
        numbers where each index position is a card rank, and its value is its
        card frequency.

        You will probably want to call the std_dev function in somewhere in
        here.

    Printing:
        Prints the statistic for each suit to the screen, see assignment page
        for an example output.

    Returns:
        None
    """
    # DO NOT REMOVE BELOW
    if type(card_freqs) != dict or \
            list(filter(lambda x: type(card_freqs[x]) != list, card_freqs)):
        raise TypeError(
            "card_freqs is required to be a dict where each value is a \
                list of ints.")
    # DO NOT REMOVE ABOVE

    print('Standard deviation for the frequency counts of each rank in suit: ')
    for key, value in card_freqs.items():
        stdev = std_dev(value)
        if key == 'd':
            suit = 'Diamonds'
        elif key == 'c':
            suit = 'Clubs'
        elif key == 'h':
            suit = 'Hearts'
        elif key == 's':
            suit = 'Spades'
        print('\t{0}: {1:.4f} cards'.format(suit, stdev))


def main():
    cards = make_random_cards()
    suit_counts = freq_count(cards)
    print_stats(suit_counts)


if __name__ == "__main__":
    main()
