import unittest
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

from HandOfCards import HandOfCards
from PlayingCard import PlayingCard

class TestHandOfCards(unittest.TestCase):
    def setUp(self):
        self.cards = [
            PlayingCard('H', 2),
            PlayingCard('H', 3),
            PlayingCard('H', 4),
            PlayingCard('H', 5),
            PlayingCard('H', 6)
        ]
        self.hand = HandOfCards(self.cards)

    def test_hand_initialization(self):
        self.assertEqual(self.hand.cards, self.cards, "Hand should be initialized with the given cards")

    def test_is_flush_true(self):
        self.assertTrue(self.hand.is_flush(), "Hand should be a flush when all cards have the same suit")

    def test_is_flush_false(self):
        non_flush_cards = [
            PlayingCard('H', 2),
            PlayingCard('H', 3),
            PlayingCard('H', 4),
            PlayingCard('H', 5),
            PlayingCard('S', 6)
        ]
        non_flush_hand = HandOfCards(non_flush_cards)
        self.assertFalse(non_flush_hand.is_flush(), "Hand should not be a flush when not all cards have the same suit")

    def test_is_flush_less_than_five_cards(self):
        less_than_five_cards = [
            PlayingCard('H', 2),
            PlayingCard('H', 3),
            PlayingCard('H', 4),
            PlayingCard('H', 5)
        ]
        small_hand = HandOfCards(less_than_five_cards)
        self.assertFalse(small_hand.is_flush(), "Hand should not be a flush when it contains less than 5 cards")

    def test_str(self):
        hand_str = str(self.hand)
        self.assertIsInstance(hand_str, str, "__str__ should return a string")
        self.assertTrue(all(card.get_as_string() in hand_str for card in self.hand.cards), "__str__ should include all cards in the hand")

if __name__ == '__main__':
    unittest.main()
