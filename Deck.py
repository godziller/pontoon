from random import shuffle

from Card import Card
import random
from PontoonCard import PontoonCard


class Deck(object):
    def __init__(self):
        self._cardlist = []
        for suit in Card.suit_list:
            for rank in Card.rank_list:
                self._cardlist.append(PontoonCard(suit,rank))

    def shuffle(self):
        random.shuffle(self._cardlist)

    def length(self):
        return len(self._cardlist)

    def deal_card(self):
        """ Remove and return the top card in the deck. """
        return self._cardlist.pop()

    def __str__(self):
            return "\n".join(str(card) for card in self._cardlist)

if __name__ == "__main__":
    my_deck = Deck()
    print(my_deck)
