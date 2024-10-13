import sys
from multiprocessing.managers import Value


class Card:
    suit_list = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    rank_list = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    def __init__(self, suit, rank):
        try:
            if suit in self.suit_list:
                self._suit = suit
            else:
                raise ValueError('Invalid Suit.')
        except ValueError:
            print('Invalid Suit')

        try:
            if rank in self.rank_list:
                self._rank = rank
            else:
                raise ValueError("Invalid Rank")
        except ValueError:
            print("Invalid Rank")

    def get_suit(self):
        return self._suit

    def get_rank(self):
        return self._rank


    def __str__(self):
        return f"the {self._rank} of {self._suit}"


if __name__ == "__main__":
    my_card = Card("Spades", "K")
    print(my_card)
    #print(my_card)
