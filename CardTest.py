from unittest import TestCase
from Card import Card

class TestCard(TestCase):
    suit = ""
    rank = ""
    def setUp(self):
        suit = 'Spades'
        self.suit = suit
        rank = 'K'
        self.rank = rank
        self.card = Card(suit, rank)



class TestInit(TestCard):

    def test_not_none(self):
        self.assertIsNot(self.card, None)

    def test_in_list(self):
        suit_list = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
        rank_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.assertIn(self.suit, suit_list)
        self.assertIn(self.rank, rank_list)

    def test_suit_set(self):
        self.assertEqual(self.suit, 'farts')


