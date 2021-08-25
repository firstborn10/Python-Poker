import random
import collections
from operator import attrgetter


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return str(self.rank) + self.suit


class Hand:
    # Initializes and ranks hand.
    def __init__(self, cards):
        self.hand = cards
        self.sorted_by_frequency = []
        self.reverse_sort = []
        self.rank = ""  # Defines rank as string.
        self.rank_number = 0  # Defines rank as integer for comparison later (initializes as high card).
        self.flush = False
        self.straight = False

        # Establishes histograms for comparison.
        quads = [4, 1]
        full_house = [3, 2]
        three_of_a_kind = [3, 1, 1]
        two_pair = [2, 2, 1]
        pair = [2, 1, 1, 1]

        # Defines a variable for easier sorting.
        rank_attr = attrgetter("rank")
        suit_attr = attrgetter("suit")

        # Sorts hands and creates histograms for comparison.
        hand_list = list(self.hand)
        dictionary_list = collections.Counter(rank_attr(r) for r in hand_list)  # Creates list of dictionaries with frequency of each rank.
        self.sorted_by_frequency = sorted(dictionary_list, key=dictionary_list.get, reverse=True)
        self.reverse_sort = sorted((rank_attr(r) for r in hand_list), reverse=True)
        histogram_hand = sorted(collections.Counter(rank_attr(r) for r in hand_list).values(), reverse=True)  # Creates histogram of hand.

        # Determines if hand is any of the following "histogram" ranks
        # (meaning there are two or more cards with the same rank).
        if histogram_hand == quads:
            self.rank = "Quads"
            self.rank_number = 8
        elif histogram_hand == full_house:
            self.rank = "Full House"
            self.rank_number = 7
        elif histogram_hand == three_of_a_kind:
            self.rank = "Three of a Kind"
            self.rank_number = 4
        elif histogram_hand == two_pair:
            self.rank = "Two Pair"
            self.rank_number = 3
        elif histogram_hand == pair:
            self.rank = "Pair"
            self.rank_number = 2
        else:

            # At this point it is determined there are no two cards with the same rank.

            # Tests for flush.
            f = sorted(collections.Counter(suit_attr(r) for r in hand_list).values())
            if f == [5]:
                self.flush = True

            # Tests for straight.
            if self.reverse_sort[0] - self.reverse_sort[4] == 4 or self.reverse_sort[0] == 14 and self.reverse_sort[1] == 5:
                self.straight = True

            # Tests for straight flush.
            if self.flush and self.straight:
                if self.reverse_sort[0] == 14:
                    self.rank = "Royal Flush"
                    self.rank_number = 10
                else:
                    self.rank = "Straight Flush"
                    self.rank_number = 9

            elif self.flush:
                self.rank = "Flush"
                self.rank_number = 6
            elif self.straight:
                self.rank = "Straight"
                self.rank_number = 5
            else:
                self.rank = "High Card"
                self.rank_number = 1

    def __repr__(self):
        return str(self.hand)


class Deck:

    def __init__(self):
        self.contents = []

    def new_deck(self):
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        suits = ["s", "h", "d", "c"]

        for s in suits:
            for r in ranks:
                c = Card(r, s)
                self.contents.append(c)

    def shuffle(self):
        random.shuffle(self.contents)

    def __repr__(self):
        return str(self.contents)


# This function takes two hands and compares them to find a winner.
def compare_two_hands(hand1, hand2):

    # Compares rank of hands to determine if one is higher than the other.
    if hand1.rank_number > hand2.rank_number:
        return hand1
    elif hand1.rank_number < hand2.rank_number:
        return hand2

    else:

        # At this point it is assumed that both hands are equal ranks (pair and pair for example).

        # Tests for tie.
        index = 0
        while index <= 4:
            if hand1.reverse_sort[index] == hand2.reverse_sort[index]:
                if index == 4:
                    return "Tie"
                else:
                    index += 1
            else:
                break

        # At this point it is assumed both hands are NOT a tie.

        # Compares high card hands and flushes.
        if hand1.rank_number == 1 or hand1.rank_number == 6:
            for card in range(len(hand1.reverse_sort)):
                if hand1.reverse_sort[card] > hand2.reverse_sort[card]:
                    return hand1
                elif hand1.reverse_sort[card] < hand2.reverse_sort[card]:
                    return hand2
                else:
                    continue

        # Compares two pair hands and kicker.
        if hand1.rank_number == 3:
            two_pair_list1 = sorted([hand1.sorted_by_frequency[0], hand1.sorted_by_frequency[1]], reverse=True)
            two_pair_list2 = sorted([hand2.sorted_by_frequency[0], hand2.sorted_by_frequency[1]], reverse=True)

            if two_pair_list1[0] > two_pair_list2[0]:
                return hand1
            elif two_pair_list1[0] < two_pair_list2[0]:
                return hand2
            elif two_pair_list1[1] > two_pair_list2[1]:
                return hand1
            elif two_pair_list1[1] < two_pair_list2[1]:
                return hand2
            elif hand1.sorted_by_frequency[2] > hand2.sorted_by_frequency[2]:
                return hand1
            else:
                return hand2

        # Tests pair, three of a kind, full house, and quads.
        if hand1.rank_number == 2 or hand1.rank_number == 4 or \
                hand1.rank_number == 7 or hand1.rank_number == 8:

            # Compares the actual pair, two pair, three of a kind, full house, or quads.
            if hand1.sorted_by_frequency[0] > hand2.sorted_by_frequency[0]:
                return hand1
            if hand1.sorted_by_frequency[0] < hand2.sorted_by_frequency[0]:
                return hand2

            # Compares kickers.
            else:
                reverse_sort_list1 = sorted(hand1.sorted_by_frequency, reverse=True)
                reverse_sort_list2 = sorted(hand2.sorted_by_frequency, reverse=True)
                for card in range(len(hand1.sorted_by_frequency)):
                    if reverse_sort_list1[card] > reverse_sort_list2[card]:
                        return hand1
                    if reverse_sort_list1[card] < reverse_sort_list2[card]:
                        return hand2
                    else:
                        continue

        # Compares straight, and straight flush.
        if hand1.rank_number == 5 or hand1.rank_number == 9:
            if hand1.reverse_sort[0] == 14 and hand1.reverse_sort[1] == 5:
                return hand2
            elif hand2.reverse_sort[0] == 14 and hand1.reverse_sort[1] == 5:
                return hand1
            elif hand1.reverse_sort[0] > hand2.reverse_sort[0]:
                return hand1
            else:
                return hand2
