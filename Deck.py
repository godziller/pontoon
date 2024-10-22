# Student Number: 123411792
from random import shuffle

from Card import Card
import random
from PontoonCard import PontoonCard

class Deck(object):

    def __init__(self):
        """
        The Deck Class represents a deck of 52 cards
        """
        suit_names = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
        rank_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        self._cardlist = []
        try:
            for suit in suit_names:
                for rank in rank_list:
                    self._cardlist.append(PontoonCard(suit,rank))
        except:
            print(f"Invalid Card Creation")


    def shuffle(self):
        """
        shuffle will randomly shuffle the deck
        :return: nothing
        """

        random.shuffle(self._cardlist)

    def length(self):
        """
        length returns the number of cards in the deck
        :return:
        """
        return len(self._cardlist)

    def deal_card(self):
        """ Remove and return the top card in the deck. """
        return self._cardlist.pop()

    def __str__(self):
            return "\n".join(str(card) for card in self._cardlist)

if __name__ == "__main__":
    my_deck = Deck()
    print(my_deck)
