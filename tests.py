from poker import Hand, Card, compare_two_hands
import unittest


class TestHands(unittest.TestCase):
    def test_high_card(self):
        cards = [Card(2, "s"), Card(3, "c"), Card(4, "s"), Card(5, "s"), Card(7, "s")]
        result = Hand(cards).rank
        self.assertEqual(result, "High Card")

    def test_pair(self):
        cards = [Card(10, "s"), Card(10, "c"), Card(4, "s"), Card(5, "s"), Card(7, "s")]
        result = Hand(cards).rank
        self.assertEqual(result, "Pair")

    def test_two_pair(self):
        cards = [Card(2, "s"), Card(2, "c"), Card(4, "s"), Card(13, "s"), Card(13, "s")]
        result = Hand(cards).rank
        self.assertEqual(result, "Two Pair")

    def test_three_of_a_kind(self):
        cards = [Card(7, "s"), Card(7, "c"), Card(7, "s"), Card(14, "s"), Card(6, "s")]
        result = Hand(cards).rank
        self.assertEqual(result, "Three of a Kind")

    def test_full_house(self):
        cards = [Card(9, "s"), Card(12, "c"), Card(12, "s"), Card(9, "s"), Card(12, "s")]
        result = Hand(cards).rank
        self.assertEqual(result, "Full House")

    def test_quads(self):
        cards = [Card(6, "s"), Card(6, "c"), Card(6, "s"), Card(5, "s"), Card(6, "s")]
        result = Hand(cards).rank
        self.assertEqual(result, "Quads")

    def test_straight(self):
        cards = [Card(2, "s"), Card(3, "c"), Card(4, "s"), Card(5, "s"), Card(6, "s")]
        result = Hand(cards).rank
        self.assertEqual(result, "Straight")

    def test_flush(self):
        cards = [Card(6, "s"), Card(3, "s"), Card(4, "s"), Card(5, "s"), Card(14, "s")]
        result = Hand(cards).rank
        self.assertEqual(result, "Flush")

    def test_straight_flush(self):
        cards = [Card(5, "d"), Card(6, "d"), Card(8, "d"), Card(9, "d"), Card(7, "d")]
        result = Hand(cards).rank
        self.assertEqual(result, "Straight Flush")

    def test_royal_flush(self):
        cards = [Card(12, "h"), Card(11, "h"), Card(13, "h"), Card(10, "h"), Card(14, "h")]
        result = Hand(cards).rank
        self.assertEqual(result, "Royal Flush")

    def test_wheel(self):
        cards = [Card(2, "s"), Card(14, "c"), Card(4, "s"), Card(5, "s"), Card(3, "s")]
        result = Hand(cards).rank
        self.assertEqual(result, "Straight")

    def test_reverse_sort(self):
        cards = [Card(2, "s"), Card(3, "c"), Card(4, "s"), Card(5, "s"), Card(6, "s")]
        result = Hand(cards).reverse_sort
        self.assertEqual(result, [6, 5, 4, 3, 2])

    def test_compare_tie(self):
        hand1 = Hand([Card(2, "s"), Card(3, "c"), Card(4, "s"), Card(5, "s"), Card(6, "s")])
        hand2 = Hand([Card(2, "s"), Card(3, "h"), Card(4, "s"), Card(5, "s"), Card(6, "s")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, "Tie")

    def test_compare_high_card(self):
        hand1 = Hand([Card(2, "s"), Card(3, "c"), Card(4, "s"), Card(5, "s"), Card(7, "s")])
        hand2 = Hand([Card(2, "s"), Card(3, "h"), Card(4, "s"), Card(5, "s"), Card(8, "s")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand2)

    def test_compare_pair(self):
        hand1 = Hand([Card(10, "s"), Card(10, "c"), Card(4, "s"), Card(5, "s"), Card(7, "s")])
        hand2 = Hand([Card(2, "s"), Card(4, "h"), Card(4, "s"), Card(5, "s"), Card(14, "s")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand1)

    def test_compare_two_pair(self):
        hand1 = Hand([Card(10, "s"), Card(11, "c"), Card(4, "s"), Card(11, "s"), Card(10, "s")])
        hand2 = Hand([Card(2, "s"), Card(2, "h"), Card(4, "s"), Card(14, "s"), Card(14, "s")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand2)

    def test_compare_three_of_a_kind(self):
        hand1 = Hand([Card(12, "s"), Card(10, "c"), Card(12, "s"), Card(12, "s"), Card(7, "s")])
        hand2 = Hand([Card(13, "s"), Card(13, "h"), Card(4, "s"), Card(13, "s"), Card(14, "s")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand2)

    def test_compare_full_house(self):
        hand1 = Hand([Card(10, "c"), Card(10, "c"), Card(11, "c"), Card(11, "c"), Card(10, "c")])
        hand2 = Hand([Card(4, "d"), Card(4, "d"), Card(4, "d"), Card(14, "d"), Card(14, "d")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand1)

    def test_compare_quads(self):
        hand1 = Hand([Card(5, "s"), Card(5, "c"), Card(4, "s"), Card(5, "s"), Card(5, "s")])
        hand2 = Hand([Card(2, "s"), Card(7, "h"), Card(7, "s"), Card(7, "s"), Card(7, "s")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand2)

    def test_compare_straight(self):
        hand1 = Hand([Card(5, "s"), Card(6, "c"), Card(7, "s"), Card(8, "s"), Card(9, "s")])
        hand2 = Hand([Card(9, "s"), Card(10, "h"), Card(11, "s"), Card(12, "s"), Card(13, "s")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand2)

    def test_compare_wheel(self):
        hand1 = Hand([Card(5, "s"), Card(4, "c"), Card(14, "s"), Card(2, "s"), Card(3, "s")])
        hand2 = Hand([Card(9, "s"), Card(10, "h"), Card(11, "s"), Card(12, "s"), Card(13, "s")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand2)

    def test_compare_straight_flush(self):
        hand1 = Hand([Card(4, "c"), Card(5, "c"), Card(6, "c"), Card(7, "c"), Card(8, "c")])
        hand2 = Hand([Card(2, "d"), Card(3, "d"), Card(4, "d"), Card(5, "d"), Card(6, "d")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand1)

    def test_compare_flush(self):
        hand1 = Hand([Card(4, "c"), Card(14, "c"), Card(6, "c"), Card(7, "c"), Card(10, "c")])
        hand2 = Hand([Card(2, "d"), Card(12, "d"), Card(4, "d"), Card(13, "d"), Card(6, "d")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand1)

    def test_hands_of_different_strength(self):
        hand1 = Hand([Card(4, "c"), Card(14, "c"), Card(6, "c"), Card(7, "c"), Card(10, "c")])
        hand2 = Hand([Card(2, "d"), Card(12, "d"), Card(4, "d"), Card(13, "d"), Card(6, "d")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand1)

    def test_compare_kicker(self):
        hand1 = Hand([Card(10, "s"), Card(11, "c"), Card(4, "s"), Card(11, "s"), Card(10, "s")])
        hand2 = Hand([Card(5, "s"), Card(11, "c"), Card(10, "s"), Card(11, "s"), Card(10, "c")])
        result = compare_two_hands(hand1, hand2)
        self.assertEqual(result, hand2)


if __name__ == '__main__':
    unittest.main()
