import unittest
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

from PlayingCard import PlayingCard


class TestPlayingCard(unittest.TestCase):
    def test_initialization_valid(self):
        card = PlayingCard('H', 10)
        self.assertEqual(card.get_suit(), 'H', "Suit should be 'H'")
        self.assertEqual(card.get_face(), 10, "Face value should be 10")

    def test_initialization_invalid_suit(self):
        with self.assertRaises(ValueError):
            PlayingCard('X', 10)

    def test_initialization_invalid_face(self):
        with self.assertRaises(ValueError):
            PlayingCard('H', 0)
        with self.assertRaises(ValueError):
            PlayingCard('H', 14)

    def test_get_as_string(self):
        card = PlayingCard('D', 5)
        self.assertEqual(card.get_as_string(), 'D5', "String representation should be 'D5'")

    def test_get_suit(self):
        card = PlayingCard('C', 7)
        self.assertEqual(card.get_suit(), 'C', "Suit should be 'C'")

    def test_get_face(self):
        card = PlayingCard('S', 13)
        self.assertEqual(card.get_face(), 13, "Face value should be 13")

    def test_equality(self):
        card1 = PlayingCard('H', 9)
        card2 = PlayingCard('H', 9)
        card3 = PlayingCard('S', 9)
        self.assertEqual(card1, card2, "Cards with the same suit and face value should be equal")
        self.assertNotEqual(card1, card3, "Cards with different suits should not be equal")

    def test_hash(self):
        card1 = PlayingCard('H', 9)
        card2 = PlayingCard('H', 9)
        card3 = PlayingCard('S', 9)
        self.assertEqual(hash(card1), hash(card2), "Hashes of equal cards should be the same")
        self.assertNotEqual(hash(card1), hash(card3), "Hashes of different cards should not be the same")

if __name__ == '__main__':
    unittest.main()