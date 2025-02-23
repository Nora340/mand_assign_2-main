import unittest
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

from DeckOfCards import DeckOfCards
from PlayingCard import PlayingCard
from HandOfCards import HandOfCards

class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 52, "Deck should contain 52 cards initially")
        suits = ['S', 'H', 'D', 'C']
        faces = range(1, 14)
        expected_cards = [PlayingCard(suit, face) for suit in suits for face in faces]
        self.assertEqual(self.deck.cards, expected_cards, "Deck should contain all 52 unique cards")

    def test_deal_hand(self):
        hand = self.deck.deal_hand(5)
        self.assertIsInstance(hand, HandOfCards, "deal_hand should return an instance of HandOfCards")
        self.assertEqual(len(hand.cards), 5, "Hand should contain 5 cards")
        self.assertEqual(len(self.deck.cards), 52, "Deck should still contain 52 cards after dealing")

    def test_deal_hand_invalid_number(self):
        with self.assertRaises(ValueError):
            self.deck.deal_hand(0)
        with self.assertRaises(ValueError):
            self.deck.deal_hand(53)

    def test_str(self):
        deck_str = str(self.deck)
        self.assertIsInstance(deck_str, str, "__str__ should return a string")
        self.assertTrue(all(card.get_as_string() in deck_str for card in self.deck.cards), "__str__ should include all cards in the deck")

if __name__ == '__main__':
    unittest.main()